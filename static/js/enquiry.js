(function () {
  "use strict";

  var form = document.getElementById("enquiryForm");
  if (!form) return;

  var statusEl = document.getElementById("formStatus");
  var submitBtn = document.getElementById("enquirySubmitBtn");
  var submitLabel = submitBtn ? submitBtn.querySelector(".btn-label") : null;
  var lang = document.documentElement.getAttribute("lang") === "ta" ? "ta" : "en";

  var STRINGS = {
    en: {
      submitting: "Submitting...",
      submit: "Submit Requirement",
      success: "Your enquiry has been submitted successfully.",
      error: "Something went wrong. Please call us directly.",
      required: "This field is required.",
      invalidPhone: "Enter a valid phone number.",
      invalidEmail: "Enter a valid email address.",
    },
    ta: {
      submitting: "அனுப்பப்படுகிறது...",
      submit: "கோரிக்கையை அனுப்பவும்",
      success: "உங்கள் கோரிக்கை வெற்றிகரமாக அனுப்பப்பட்டது.",
      error: "ஏதோ தவறு நேர்ந்தது. தயவுசெய்து எங்களை நேரடியாக அழைக்கவும்.",
      required: "இந்த புலம் அவசியம்.",
      invalidPhone: "சரியான தொலைபேசி எண்ணை உள்ளிடவும்.",
      invalidEmail: "சரியான மின்னஞ்சல் முகவரியை உள்ளிடவும்.",
    },
  }[lang];

  var PHONE_RE = /^[0-9+\-\s()]{7,20}$/;
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function setFieldError(field, message) {
    var group = field.closest(".form-group");
    var errorEl = group ? group.querySelector(".form-error") : null;
    if (group) group.classList.toggle("has-error", !!message);
    if (errorEl) errorEl.textContent = message || "";
  }

  function validate() {
    var valid = true;

    ["name", "phone", "location", "service", "message"].forEach(function (name) {
      var field = form.elements[name];
      if (!field) return;
      if (!field.value || !field.value.trim()) {
        setFieldError(field, STRINGS.required);
        valid = false;
      } else {
        setFieldError(field, "");
      }
    });

    var phoneField = form.elements["phone"];
    if (phoneField && phoneField.value && !PHONE_RE.test(phoneField.value.trim())) {
      setFieldError(phoneField, STRINGS.invalidPhone);
      valid = false;
    }

    var emailField = form.elements["email"];
    if (emailField && emailField.value && !EMAIL_RE.test(emailField.value.trim())) {
      setFieldError(emailField, STRINGS.invalidEmail);
      valid = false;
    }

    return valid;
  }

  form.querySelectorAll("input, select, textarea").forEach(function (field) {
    field.addEventListener("blur", validate);
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    if (!validate()) {
      statusEl.textContent = "";
      var firstError = form.querySelector(".has-error input, .has-error select, .has-error textarea");
      if (firstError) firstError.focus();
      return;
    }

    var payload = {
      name: form.elements["name"].value.trim(),
      company_name: form.elements["company_name"].value.trim() || null,
      phone: form.elements["phone"].value.trim(),
      email: form.elements["email"].value.trim() || null,
      location: form.elements["location"].value.trim(),
      service: form.elements["service"].value,
      workers_or_vehicles: form.elements["workers_or_vehicles"].value.trim() || null,
      message: form.elements["message"].value.trim(),
      language: lang,
      website: form.elements["website"] ? form.elements["website"].value : "",
    };

    submitBtn.disabled = true;
    if (submitLabel) submitLabel.textContent = STRINGS.submitting;
    statusEl.textContent = "";
    statusEl.className = "form-status";

    fetch("/api/enquiry", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })
      .then(function (res) {
        return res.json().then(function (data) {
          return { ok: res.ok, data: data };
        });
      })
      .then(function (result) {
        if (result.ok && result.data.success) {
          statusEl.textContent = result.data.message || STRINGS.success;
          statusEl.className = "form-status is-success";
          form.reset();
        } else {
          statusEl.textContent = result.data.message || STRINGS.error;
          statusEl.className = "form-status is-error";
        }
      })
      .catch(function () {
        statusEl.textContent = STRINGS.error;
        statusEl.className = "form-status is-error";
      })
      .finally(function () {
        submitBtn.disabled = false;
        if (submitLabel) submitLabel.textContent = STRINGS.submit;
      });
  });
})();
