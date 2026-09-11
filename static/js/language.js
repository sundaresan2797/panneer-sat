(function () {
  "use strict";

  // Remember the visitor's last chosen language so a future direct visit to
  // "/" can be pointed at it (root always defaults to /en/ server-side).
  var currentLang = document.documentElement.getAttribute("lang");
  try {
    if (currentLang === "en" || currentLang === "ta") {
      localStorage.setItem("sat_lang_pref", currentLang);
    }
  } catch (e) {
    /* localStorage unavailable (private mode etc.) — safe to ignore */
  }
})();
