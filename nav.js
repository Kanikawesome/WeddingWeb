/* ==========================================================================
   SHARED SITE HEADER
   Injects the navigation bar into every page that has a <div id="site-header">
   placeholder (every page except the home page, which has its own hero nav).
   Styling lives in theme.css under the .site-nav rules.
   ========================================================================== */
(function () {
  var mount = document.getElementById('site-header');
  if (!mount) return;

  var links = [
    { href: 'travel.html',    label: 'Travel &amp; Stay' },
    { href: 'itinerary.html', label: 'Itinerary' },
    { href: 'registry.html',  label: 'Registry' },
    { href: 'gallery.html',   label: 'Our Story' },
    { href: 'faq.html',       label: 'FAQ' },
    { href: 'rsvp.html',      label: 'RSVP' }
  ];

  var current = (location.pathname.split('/').pop() || '').toLowerCase();

  var items = links.map(function (l) {
    var active = l.href === current ? ' class="active"' : '';
    return '<li><a href="' + l.href + '"' + active + '>' + l.label + '</a></li>';
  }).join('');

  mount.innerHTML =
    '<nav class="site-nav" aria-label="Main navigation">' +
      '<a href="index.html" class="nav-logo">S &amp; N</a>' +
      '<button class="nav-toggle" id="nav-toggle-btn" type="button" aria-expanded="false" aria-controls="nav-menu">Menu</button>' +
      '<ul class="nav-links" id="nav-menu">' + items + '</ul>' +
    '</nav>';

  var toggle = document.getElementById('nav-toggle-btn');
  var menu = document.getElementById('nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
})();
