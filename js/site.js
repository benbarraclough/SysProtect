(() => {
  'use strict';
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.getElementById('primary-nav');
  if (toggle && menu) {
    const closeMenu = () => { toggle.setAttribute('aria-expanded', 'false'); toggle.setAttribute('aria-label', 'Open navigation'); menu.classList.remove('is-open'); };
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      menu.classList.toggle('is-open', open);
    });
    menu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
    document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
    document.addEventListener('click', event => { if (!menu.contains(event.target) && !toggle.contains(event.target)) closeMenu(); });
  }
  const year = document.getElementById('copyright-year');
  if (year) year.textContent = String(new Date().getFullYear());

  // Only expose a business address after the site owner explicitly configures one.
  const configured = typeof window.SYSPROTECT_CONTACT_EMAIL === 'string' ? window.SYSPROTECT_CONTACT_EMAIL.trim() : '';
  const validAddress = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(configured) && !configured.includes('<') && !configured.includes('>');
  const cta = document.getElementById('contact-cta');
  const note = document.getElementById('contact-note');
  if (validAddress && cta) {
    cta.href = 'mailto:' + configured + '?subject=' + encodeURIComponent('SysProtect project enquiry');
    cta.removeAttribute('target');
    cta.removeAttribute('rel');
    cta.innerHTML = 'Email SysProtect <span aria-hidden="true">↗</span>';
    if (note) note.textContent = 'Share a short summary of your requirements, and include any preferred times for an initial conversation. Please do not email passwords or other sensitive information.';
  }
})();
