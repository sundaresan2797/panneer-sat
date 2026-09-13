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

  var prefersReducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Subtle reveal-on-scroll for section headers and cards, staggered per
  // item within its own grid so a row cascades in rather than popping at once.
  var revealTargets = document.querySelectorAll(
    ".service-card, .capability-card, .why-card, .industry-card, .corporate-req-card, .info-card, .contact-card, .trust-item"
  );
  if ("IntersectionObserver" in window && revealTargets.length) {
    var groupCounts = new Map();
    revealTargets.forEach(function (el) {
      el.classList.add("reveal");
      var count = groupCounts.get(el.parentElement) || 0;
      if (count > 0) el.style.transitionDelay = Math.min(count * 70, 420) + "ms";
      groupCounts.set(el.parentElement, count + 1);
    });
    var revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealTargets.forEach(function (el) { revealObserver.observe(el); });
  }

  // Count-up: any element carrying .count-up with text starting in a number
  // (e.g. "5+ Years Experience") animates that leading number from 0 when it
  // scrolls into view. Non-numeric text is left untouched.
  var countTargets = document.querySelectorAll(".count-up");
  countTargets.forEach(function (el) {
    var match = el.textContent.match(/^(\d+)(.*)$/);
    if (!match) return;
    var target = parseInt(match[1], 10);
    var suffix = match[2];
    var numberSpan = document.createElement("span");
    numberSpan.className = "count-num";
    numberSpan.textContent = prefersReducedMotion ? String(target) : "0";
    el.textContent = "";
    el.appendChild(numberSpan);
    el.appendChild(document.createTextNode(suffix));

    if (prefersReducedMotion || !("IntersectionObserver" in window)) return;

    var countObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          countObserver.unobserve(entry.target);
          var start = null;
          var duration = 900;
          function step(timestamp) {
            if (start === null) start = timestamp;
            var progress = Math.min((timestamp - start) / duration, 1);
            numberSpan.textContent = Math.round(progress * target);
            if (progress < 1) window.requestAnimationFrame(step);
          }
          window.requestAnimationFrame(step);
        });
      },
      { threshold: 0.4 }
    );
    countObserver.observe(el);
  });

  // Subtle parallax drift on the hero image as the page scrolls.
  var heroImageFrame = document.querySelector(".hero-image-frame");
  if (heroImageFrame && !prefersReducedMotion) {
    var ticking = false;
    window.addEventListener(
      "scroll",
      function () {
        if (ticking) return;
        ticking = true;
        window.requestAnimationFrame(function () {
          var offset = Math.min(window.scrollY * 0.12, 40);
          heroImageFrame.style.transform = "translateY(" + offset + "px)";
          ticking = false;
        });
      },
      { passive: true }
    );
  }

  // Intro video: click-to-play (no autoplay, no preload) — native controls
  // only appear once the visitor actually starts playback.
  var introVideo = document.getElementById("introVideo");
  var videoPlayBtn = document.getElementById("videoPlayBtn");
  if (introVideo && videoPlayBtn) {
    videoPlayBtn.addEventListener("click", function () {
      introVideo.setAttribute("controls", "");
      introVideo.play();
      videoPlayBtn.hidden = true;
    });
  }
})();
