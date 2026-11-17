# SysProtect website

A lightweight, responsive one-page website for SysProtect, an independent cyber security consultancy based in Manchester, UK.

## What's included

- Nine service areas including threat assessments, incident response, vulnerability management, web security, security monitoring, access management, hardening, policy and contract support
- Service, process, about, FAQ and contact sections
- Responsive mobile navigation, keyboard-visible focus indicators and reduced-motion support
- Accessible HTML, SEO metadata and SVG favicon
- No third-party scripts, font CDNs, trackers, build step or paid hosting requirement
- Redirects for old about, service, blog and contact URLs so obsolete template pages are not exposed

## Before publishing to clients

**1. Enquiries (optional for now).** No email is needed to publish the site. It clearly states that enquiries are not yet open; the profile link is for background only, not for emergency reporting. To enable email enquiries later, set an approved **business** email in `config.js` using `window.SYSPROTECT_CONTACT_EMAIL`. This converts the contact CTA into a `mailto:` link without needing a new form.

**2. Confirm the offer.** Review the services and geographic/remote wording against actual skills, insurance, capacity and preferred client work. None of the listed service areas is a guarantee of specific certifications or accreditations.

**3. Add legal and company details as appropriate.** Add registered business/company identity, trading address if legally required, privacy notice and other required trading information once the business structure and contact method are decided. Avoid collecting personal data in an unverified form.

**4. Set a domain if wanted.** The site works on a GitHub Pages project URL using relative asset paths. If you add a custom domain, configure it in repository Pages settings and use a matching CNAME. Add canonical and social preview metadata once the final URL is known.

## Preview / deploy

For a local static preview, from the repository root:

```bash
python3 -m http.server 8000
```

Visit http://localhost:8000. GitHub Pages can publish the `main` branch at `/(root)`; check **Settings → Pages** to confirm the publishing source. No build is required.

## Files

- `index.html` — site content
- `css/site.css` — styles and responsive layouts
- `js/site.js` — mobile nav and business email behaviour
- `config.js` — public business email configuration
- `favicon.svg` — identity mark
- `about.html`, `service.html`, `contact.html`, `blog.html` — legacy URL redirects

The obsolete HTML theme libraries, stock images, fonts and large video files have been removed from the current tree to keep the site maintainable. Git history still preserves earlier versions for recovery.
