(function () {
  function ensureLightbox() {
    var existing = document.querySelector('.ldb-lightbox');
    if (existing) return existing;

    var overlay = document.createElement('div');
    overlay.className = 'ldb-lightbox';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');

    var img = document.createElement('img');
    img.className = 'ldb-lightbox__img';
    img.alt = '';

    overlay.appendChild(img);
    document.body.appendChild(overlay);

    function close() {
      overlay.classList.remove('is-open');
      img.removeAttribute('src');
    }

    overlay.addEventListener('click', close);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });

    overlay._ldbOpen = function (src) {
      img.src = src;
      overlay.classList.add('is-open');
    };

    return overlay;
  }

  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a.js-lightbox') : null;
    if (!a) return;

    var href = a.getAttribute('href');
    if (!href) return;

    e.preventDefault();
    var lb = ensureLightbox();
    lb._ldbOpen(href);
  });
})();
