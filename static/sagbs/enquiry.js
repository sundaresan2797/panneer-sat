(() => {
  'use strict';
  const form = document.getElementById('sagbsEnquiry');
  if (!form) return;
  const status = document.getElementById('sagbsFormStatus');
  const submit = document.getElementById('sagbsSubmit');
  const submitLabel = submit.querySelector('span');
  const originalLabel = submitLabel.textContent;
  const newId = () => window.crypto?.randomUUID ? crypto.randomUUID() : 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => { const r = Math.random() * 16 | 0; return (c === 'x' ? r : (r & 3 | 8)).toString(16); });
  let submissionId = newId();
  let lastFingerprint = '';
  let sending = false;

  function fieldError(name, message) {
    const field = form.elements[name];
    if (!field) return;
    field.setAttribute('aria-invalid', String(Boolean(message)));
    const target = document.getElementById(`${name}Error`);
    if (target) target.textContent = message || '';
  }
  function validate() {
    let valid = true;
    const rules = {
      name: (v) => v.length >= 2 && v.length <= 100 ? '' : 'Enter your name using 2–100 letters, numbers or spaces.',
      email: () => form.elements.email.validity.valid && form.elements.email.value.trim() ? '' : 'Check your email address. For example: name@example.com.',
      phone: (v) => /^[+\d\s().-]+$/.test(v) && v.replace(/\D/g, '').length >= 7 && v.replace(/\D/g, '').length <= 15 ? '' : 'Enter 7–15 numbers, with your country code. For example: +91 9876543210.',
      country: (v) => v.length >= 2 && v.length <= 100 ? '' : 'Enter your country name using 2–100 letters or spaces.',
      service: (v) => v ? '' : 'Choose a service or “Help me choose”.',
      message: (v) => v.length >= 20 && v.length <= 5000 ? '' : 'Tell us what work you need done. Write 20–5,000 letters, numbers or spaces.',
      consent: () => form.elements.consent.checked ? '' : 'Please tick this box so we can use your details to reply.',
    };
    Object.entries(rules).forEach(([name, rule]) => {
      const error = rule(form.elements[name].value.trim());
      fieldError(name, error);
      if (error) valid = false;
    });
    return valid;
  }
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (sending) return;
    status.textContent = '';
    status.className = 'form-status';
    if (!validate()) { form.querySelector('[aria-invalid="true"]')?.focus(); return; }
    const payload = Object.fromEntries(new FormData(form));
    payload.consent = form.elements.consent.checked;
    payload.kind = form.dataset.kind;
    const fingerprint = JSON.stringify(payload);
    if (lastFingerprint && lastFingerprint !== fingerprint) submissionId = newId();
    lastFingerprint = fingerprint;
    payload.submission_id = submissionId;
    sending = true;
    submit.disabled = true;
    submitLabel.textContent = 'Sending your message…';
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 25000);
    try {
      const response = await fetch('/sagbs/api/enquiries', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload), signal: controller.signal });
      const data = await response.json();
      if (!response.ok || !data.success) {
        if (data.errors) Object.entries(data.errors).forEach(([name, message]) => fieldError(name, message));
        throw new Error(data.message || (typeof data.detail === 'string' ? data.detail : '') || 'We could not save your message. Please try again or email us.');
      }
      status.className = 'form-status is-success';
      status.textContent = data.message + (data.reference ? ` Your message number: ${data.reference}.` : '');
      form.reset();
      submissionId = newId();
      lastFingerprint = '';
    } catch (error) {
      status.className = 'form-status is-error';
      status.textContent = error.name === 'AbortError' ? 'We could not confirm whether your message was saved. You can try sending it again or email us.' : error.message || 'Could not connect. Check your internet and try again, or email us.';
    } finally {
      clearTimeout(timeout);
      sending = false;
      submit.disabled = false;
      submitLabel.textContent = originalLabel;
      status.focus();
    }
  });
  form.querySelectorAll('input, textarea, select').forEach((field) => {
    field.addEventListener('input', () => { if (field.getAttribute('aria-invalid') === 'true') fieldError(field.name, ''); });
  });
  document.getElementById('enquiryFallback').hidden = true;
  form.hidden = false;
})();
