(function () {
  "use strict";

  // Remember SAT's language independently of the company selection page.
  var currentLang = document.documentElement.getAttribute("lang");
  try {
    if (currentLang === "en" || currentLang === "ta") {
      localStorage.setItem("sat_lang_pref", currentLang);
    }
  } catch (e) {
    /* localStorage unavailable (private mode etc.) — safe to ignore */
  }
})();
