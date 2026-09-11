(function () {
  "use strict";

  var header = document.getElementById("site-header");
  var navToggle = document.getElementById("navToggle");
  var navMenu = document.getElementById("siteNavMenu");
  var backToTop = document.getElementById("back-to-top");

  function onScroll() {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 8);
    if (backToTop) backToTop.classList.toggle("is-visible", window.scrollY > 500);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", function () {
      var isOpen = navMenu.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      document.body.style.overflow = isOpen ? "hidden" : "";
    });

    navMenu.querySelectorAll(".nav-link, .dropdown-panel a, .btn-quote").forEach(function (link) {
      link.addEventListener("click", function () {
        navMenu.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });
  }

  // Mobile: tap the "Services" nav item once to reveal its dropdown instead of navigating.
  document.querySelectorAll(".nav-item-dropdown > .nav-link").forEach(function (link) {
    link.addEventListener("click", function (e) {
      if (window.innerWidth >= 992) return;
      var item = link.closest(".nav-item-dropdown");
      if (!item.classList.contains("is-open")) {
        e.preventDefault();
        item.classList.add("is-open");
      }
    });
  });

  // WhatsApp buttons rendered before WHATSAPP_NUMBER is configured point to
  // a dead "https://wa.me/" link. Redirect those to a phone call instead so
  // nothing on the site is ever a dead click while the number is pending.
  document.querySelectorAll('[data-whatsapp-configured="false"]').forEach(function (el) {
    var fallback = el.getAttribute("data-fallback-tel");
    if (!fallback) return;
    el.setAttribute("href", fallback);
    el.removeAttribute("target");
    el.removeAttribute("rel");
  });

  if (backToTop) {
    backToTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // Subtle reveal-on-scroll for section headers and cards.
  var revealTargets = document.querySelectorAll(
    ".service-card, .capability-card, .why-card, .industry-card, .corporate-req-card, .info-card, .contact-card"
  );
  if ("IntersectionObserver" in window && revealTargets.length) {
    revealTargets.forEach(function (el) { el.classList.add("reveal"); });
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealTargets.forEach(function (el) { observer.observe(el); });
  }
})();
