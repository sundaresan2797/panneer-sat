/* Progressive enhancement: every page stays readable without animation libraries. */
(() => {
  'use strict';
  const header = document.getElementById('sagbsHeader');
  const onScroll = () => header?.classList.toggle('is-scrolled', window.scrollY > 12);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const nav = document.getElementById('sagbsNav');
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav?.classList.contains('show') && window.bootstrap) {
      bootstrap.Collapse.getOrCreateInstance(nav).hide();
      document.querySelector('.navbar-toggler')?.focus();
    }
  });

  const tabs = [...document.querySelectorAll('[data-workspace-tab]')];
  const activateTab = (tab) => {
    tabs.forEach((item) => {
      const selected = item === tab;
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
      document.getElementById(item.getAttribute('aria-controls')).hidden = !selected;
    });
  };
  if (tabs.length) {
    tabs.forEach((tab) => {
      const panel = document.getElementById(tab.getAttribute('aria-controls'));
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('aria-labelledby', tab.id);
      panel.tabIndex = 0;
    });
    activateTab(tabs[0]);
    tabs[0].closest('[role="tablist"]').hidden = false;
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => activateTab(tab));
    tab.addEventListener('keydown', (event) => {
      let next;
      if (event.key === 'ArrowRight') next = tabs[(index + 1) % tabs.length];
      if (event.key === 'ArrowLeft') next = tabs[(index + tabs.length - 1) % tabs.length];
      if (event.key === 'Home') next = tabs[0];
      if (event.key === 'End') next = tabs[tabs.length - 1];
      if (next) { event.preventDefault(); activateTab(next); next.focus(); }
    });
  });

  const filters = document.querySelectorAll('[data-project-filter]');
  const samples = document.querySelectorAll('[data-project-type]');
  filters.forEach((button) => {
    button.addEventListener('click', () => {
      const filter = button.dataset.projectFilter;
      filters.forEach((item) => {
        item.setAttribute('aria-pressed', String(item === button));
      });
      let visible = 0;
      samples.forEach((card) => {
        card.hidden = filter !== 'all' && card.dataset.projectType !== filter;
        if (!card.hidden) visible++;
      });
      document.getElementById('sampleCount').textContent =
        visible === 1 ? '1 example shown.' : visible + ' examples shown.';
      window.ScrollTrigger?.refresh();
    });
  });
  if (filters.length) document.getElementById('sampleFilters').hidden = false;

  if (!window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);
  const motion = gsap.matchMedia();
  motion.add('(prefers-reduced-motion: no-preference)', () => {
    gsap.from('[data-intro]', { y: 22, opacity: 0, duration: 0.75, stagger: 0.09, ease: 'power2.out', clearProps: 'opacity,transform' });
    document.querySelectorAll('[data-reveal]').forEach((element) => {
      gsap.from(element, { y: 22, opacity: 0, duration: 0.6, ease: 'power2.out', clearProps: 'opacity,transform', scrollTrigger: { trigger: element, start: 'top 96%', once: true } });
    });
    const bars = document.querySelector('.sheet-bars');
    if (bars) gsap.from(bars.querySelectorAll('.sheet-track i'), {
      scaleX: 0, transformOrigin: 'left center', stagger: 0.08, duration: 0.55,
      clearProps: 'transform', scrollTrigger: { trigger: '.sample-sheet', start: 'top 85%', once: true }
    });
    let illustration;
    const lottieNode = document.getElementById('workflowLottie');
    if (lottieNode && window.lottie) {
      ScrollTrigger.create({
        trigger: lottieNode, start: 'top 96%', once: true,
        onEnter: () => {
          illustration = lottie.loadAnimation({ container: lottieNode, renderer: 'svg', loop: false, autoplay: true, path: '/static/sagbs/workflow.json', rendererSettings: { progressiveLoad: true } });
          illustration.addEventListener('DOMLoaded', () => lottieNode.querySelector('.bi')?.remove());
        }
      });
    }
    return () => {
      illustration?.destroy();
      if (lottieNode) lottieNode.innerHTML = '<i class="bi bi-check2" aria-hidden="true"></i>';
    };
  });
  motion.add('(min-width: 992px) and (pointer: fine) and (prefers-reduced-motion: no-preference)', () => {
    if (!window.Lenis) return;
    const lenis = new Lenis({ duration: 0.85, smoothWheel: true, anchors: { offset: -105 }, stopInertiaOnNavigate: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.lagSmoothing(0);
    const tick = (seconds) => lenis.raf(seconds * 1000);
    gsap.ticker.add(tick);
    return () => { gsap.ticker.remove(tick); lenis.destroy(); };
  });
  if (document.fonts) document.fonts.ready.then(() => ScrollTrigger.refresh());
  window.addEventListener('pageshow', () => ScrollTrigger.refresh());
})();
