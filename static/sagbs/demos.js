(() => {
  'use strict';
  const periods = [
    { month: 'January', shipments: 232, onTime: 207, exceptions: 11 },
    { month: 'February', shipments: 244, onTime: 221, exceptions: 13 },
    { month: 'March', shipments: 248, onTime: 226, exceptions: 10 },
    { month: 'April', shipments: 265, onTime: 246, exceptions: 9 },
    { month: 'May', shipments: 281, onTime: 263, exceptions: 12 },
    { month: 'June', shipments: 272, onTime: 255, exceptions: 8 },
  ];
  const periodSelect = document.getElementById('demoPeriod');
  if (periodSelect) {
    function updateDashboard() {
      const rows = periodSelect.value === 'q1' ? periods.slice(0, 3) : periodSelect.value === 'q2' ? periods.slice(3) : periods;
      const total = rows.reduce((sum, row) => sum + row.shipments, 0);
      const delivered = rows.reduce((sum, row) => sum + row.onTime, 0);
      const exceptions = rows.reduce((sum, row) => sum + row.exceptions, 0);
      document.getElementById('demoShipments').textContent = total.toLocaleString('en-IN');
      document.getElementById('demoOnTime').textContent = `${(delivered / total * 100).toFixed(1)}%`;
      document.getElementById('demoExceptions').textContent = exceptions;
      document.getElementById('demoBars').innerHTML = rows.map((row) => `<div class="demo-bar-col"><b>${row.shipments}</b><span style="--height:${row.shipments / 300 * 75}%"></span><small>${row.month.slice(0, 3)}</small></div>`).join('');
      document.getElementById('demoBars').setAttribute('aria-label', rows.map((row) => `${row.month}: ${row.shipments} deliveries`).join(', '));
      document.getElementById('demoTableBody').innerHTML = rows.map((row) => `<tr><th scope="row">${row.month}</th><td>${row.shipments}</td><td>${row.onTime}</td><td>${row.exceptions}</td></tr>`).join('');
      document.getElementById('demoAnalyticsStatus').textContent = `${periodSelect.selectedOptions[0].textContent}: ${total} sample deliveries, ${exceptions} problems to check. All figures are made up.`;
    }
    periodSelect.addEventListener('change', updateDashboard);
    updateDashboard();
  }

  const workflow = document.getElementById('invoiceDemo');
  if (workflow) {
    const invoices = [
      { number: 'DEMO-101', vendor: 'Sample Supplier A', amount: 12500 },
      { number: 'DEMO-102', vendor: 'Sample Supplier B', amount: 8400 },
      { number: 'DEMO-101', vendor: 'Sample Supplier A', amount: 12500 },
      { number: 'DEMO-104', vendor: '', amount: 3200 },
      { number: 'DEMO-105', vendor: 'Sample Supplier C', amount: -500 },
    ];
    const run = document.getElementById('runInvoiceWorkflow');
    const download = document.getElementById('downloadInvoiceCSV');
    const status = document.getElementById('workflowStatus');
    let processed = false;
    let validRows = [];
    function render(validate) {
      const seen = new Set();
      validRows = [];
      document.getElementById('invoiceRows').innerHTML = invoices.map((invoice) => {
        let issue = '';
        if (seen.has(invoice.number)) issue = 'Repeated bill number';
        else if (!invoice.vendor) issue = 'Supplier name missing';
        else if (invoice.amount <= 0) issue = 'Check this amount';
        seen.add(invoice.number);
        if (!issue) validRows.push(invoice);
        return `<tr><th scope="row">${invoice.number}</th><td>${invoice.vendor || '—'}</td><td>${invoice.amount.toLocaleString('en-IN')}</td><td class="${validate ? (issue ? 'row-error' : 'row-valid') : ''}">${validate ? issue || 'No errors found' : 'Not checked'}</td></tr>`;
      }).join('');
    }
    run.addEventListener('click', () => {
      processed = true;
      render(true);
      download.disabled = false;
      status.textContent = `${invoices.length} sample records checked. ${validRows.length} have no errors and can be downloaded. ${invoices.length - validRows.length} need checking. No files were sent to us.`;
      window.ScrollTrigger?.refresh();
    });
    document.getElementById('resetInvoiceWorkflow').addEventListener('click', () => {
      processed = false;
      render(false);
      download.disabled = true;
      status.textContent = 'Click the button to check the sample bills.';
    });
    download.addEventListener('click', () => {
      if (!processed) return;
      const csv = ['Bill number,Supplier,Amount (rupees)', ...validRows.map((invoice) => `${invoice.number},${invoice.vendor},${invoice.amount}`)].join('\r\n');
      const url = URL.createObjectURL(new Blob([csv], { type: 'text/csv;charset=utf-8;' }));
      const link = document.createElement('a');
      link.href = url;
      link.download = 'sagbs-fictional-invoice-demo.csv';
      link.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      status.textContent = 'Your download contains the sample rows with no errors. You can open the CSV file in Excel.';
    });
    render(false);
  }
})();
