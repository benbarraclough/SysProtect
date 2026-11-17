#!/usr/bin/env python3
"""Static safety / integrity checks for the dependency-free GitHub Pages site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "about.html", "service.html", "contact.html", "blog.html"]
REQUIRED_SECTIONS = {"main", "services", "approach", "about", "questions", "contact"}
errors = []


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.title_count = 0
        self.description_count = 0
        self.viewport_count = 0
        self.html_lang = False
        self.script_sources = []
        self.forms = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "html" and attrs.get("lang") == "en-GB":
            self.html_lang = True
        if tag == "title":
            self.title_count += 1
        if tag == "meta" and attrs.get("name") == "description":
            self.description_count += 1
        if tag == "meta" and attrs.get("name") == "viewport":
            self.viewport_count += 1
        if tag == "form":
            self.forms += 1
        for name in ("href", "src"):
            if name in attrs:
                self.links.append(attrs[name])
        if tag == "script" and "src" in attrs:
            self.script_sources.append(attrs["src"])


main = SiteParser()
main.feed((ROOT / "index.html").read_text(encoding="utf-8"))

if not main.html_lang:
    errors.append("Homepage has no English-language declaration")
if main.title_count != 1 or main.description_count != 1 or main.viewport_count != 1:
    errors.append("Homepage is missing/duplicating required page metadata")
if len(main.ids) != len(set(main.ids)):
    errors.append("Duplicate homepage IDs")
if not REQUIRED_SECTIONS.issubset(main.ids):
    errors.append("Missing sections: " + ", ".join(sorted(REQUIRED_SECTIONS - set(main.ids))))
if main.forms:
    errors.append("Unconfigured contact forms must not be published")
if any(src.startswith("http:") or src.startswith("https:") for src in main.script_sources):
    errors.append("Unexpected externally hosted JavaScript")

for link in main.links:
    parts = urlsplit(link)
    if parts.scheme or parts.netloc or link.startswith("//"):
        continue
    if link.startswith("#"):
        if unquote(link[1:]) not in main.ids:
            errors.append(f"Broken in-page anchor: {link}")
        continue
    path = unquote(parts.path).lstrip("/")
    if not path:
        continue
    target = (ROOT / path).resolve()
    if ROOT not in target.parents and target != ROOT:
        errors.append(f"Link escapes repository root: {link}")
    elif not target.is_file():
        errors.append(f"Missing local file: {link}")
    if parts.fragment and path.endswith("index.html") and parts.fragment not in main.ids:
        errors.append(f"Broken cross-page anchor: {link}")

for page in PAGES[1:]:
    content = (ROOT / page).read_text(encoding="utf-8")
    if 'http-equiv="refresh"' not in content or "index.html#" not in content:
        errors.append(f"Legacy page missing redirect: {page}")

source = (ROOT / "index.html").read_text(encoding="utf-8").lower()
for forbidden in ("lorem ipsum", "joans mark", "seo agency", "projects completed", "free html templates"):
    if forbidden in source:
        errors.append(f"Old template content remains: {forbidden}")

if errors:
    print("FAILED website checks:")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)
print(f"Passed: {len(PAGES)} pages, {len(main.ids)} IDs, {len(main.links)} links, local assets and metadata.")
