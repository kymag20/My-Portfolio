(function () {
  const glow = document.getElementById('glow');
  if (glow) {
    document.addEventListener('mousemove', (e) => {
      glow.style.left = e.clientX + 'px';
      glow.style.top = e.clientY + 'px';
    });
  }

  const nav = document.getElementById('nav');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  });

  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  const mobileClose = document.getElementById('mobileClose');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => mobileMenu.classList.add('open'));
    mobileClose.addEventListener('click', () => mobileMenu.classList.remove('open'));
    mobileMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => mobileMenu.classList.remove('open'));
    });
  }

  const revealEls = document.querySelectorAll('.reveal, .stat');
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    },
    { threshold: 0.12 }
  );
  revealEls.forEach((el) => observer.observe(el));

  document.querySelectorAll('.case-header').forEach((header) => {
    header.addEventListener('click', () => {
      const item = header.closest('.case-item');
      const body = item.querySelector('.case-body');
      const isOpen = item.classList.contains('open');

      document.querySelectorAll('.case-item.open').forEach((openItem) => {
        if (openItem !== item) {
          openItem.classList.remove('open');
          openItem.querySelector('.case-body').style.maxHeight = '0';
        }
      });

      if (isOpen) {
        item.classList.remove('open');
        body.style.maxHeight = '0';
      } else {
        item.classList.add('open');
        body.style.maxHeight = body.scrollHeight + 'px';
      }
    });
  });

  const form = document.getElementById('contactForm');
  const toast = document.getElementById('toast');
  if (form && toast) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      toast.classList.add('show');
      form.reset();
      setTimeout(() => toast.classList.remove('show'), 4000);
    });
  }

  const certLightbox = document.getElementById('certLightbox');
  const certLightboxImage = document.getElementById('certLightboxImage');
  const certLightboxTitle = document.getElementById('certLightboxTitle');
  const certLightboxClose = document.getElementById('certLightboxClose');
  const certLightboxBackdrop = document.getElementById('certLightboxBackdrop');

  function openCertLightbox(title, imageUrl) {
    if (!certLightbox || !certLightboxImage || !certLightboxTitle) return;
    certLightboxTitle.textContent = title;
    certLightboxImage.src = imageUrl;
    certLightboxImage.alt = title;
    certLightbox.classList.add('open');
    certLightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeCertLightbox() {
    if (!certLightbox) return;
    certLightbox.classList.remove('open');
    certLightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('.certificate-card').forEach((card) => {
    card.addEventListener('click', () => {
      openCertLightbox(card.dataset.certTitle, card.dataset.certImage);
    });
  });

  if (certLightboxClose) certLightboxClose.addEventListener('click', closeCertLightbox);
  if (certLightboxBackdrop) certLightboxBackdrop.addEventListener('click', closeCertLightbox);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeCertLightbox();
  });
})();
