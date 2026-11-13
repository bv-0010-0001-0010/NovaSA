/**
 * Nova Construction Solutions — enquiry form handler
 * ---------------------------------------------------
 * Free Google Apps Script web app. It does three things:
 *   1. Appends every enquiry to a Google Sheet
 *   2. Emails you a notification
 *   3. Sends the enquirer a plain confirmation
 *
 * Setup instructions: see SETUP.md in this folder.
 */

// ---------------------------------------------------------------
// SETTINGS — change these three lines and nothing else.
// ---------------------------------------------------------------
const SHEET_ID    = 'PASTE_YOUR_GOOGLE_SHEET_ID_HERE';
const NOTIFY_TO   = 'admin@novaconstructions.com.au';

const BUSINESS    = 'Nova Construction Solutions SA';
const SHEET_NAME  = 'Enquiries';

const COLUMNS = [
  'Received', 'Type', 'Name', 'Company', 'Email', 'Phone',
  'Trade', 'Site suburb', 'Start date', 'Duration', 'Details', 'Consent', 'Page'
];

// ---------------------------------------------------------------

function doPost(e) {
  try {
    if (!e || !e.postData || !e.postData.contents) {
      return json({ status: 'error', message: 'No data received.' });
    }

    const data = JSON.parse(e.postData.contents);

    // Honeypot — bots fill hidden fields, people don't.
    if (data.company_website) {
      return json({ status: 'ok', message: 'Thanks.' });
    }

    // Minimum viable enquiry
    if (!data.name || !data.email || !data.message) {
      return json({ status: 'error', message: 'Name, email and details are required.' });
    }
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(String(data.email))) {
      return json({ status: 'error', message: 'That email address does not look right.' });
    }

    const received = new Date();
    const row = [
      received,
      data.enquiry_type || 'General enquiry',
      clean(data.name),
      clean(data.company),
      clean(data.email),
      clean(data.phone),
      clean(data.trade),
      clean(data.suburb),
      clean(data.start_date),
      clean(data.duration),
      clean(data.message),
      data.consent ? 'Yes' : 'No',
      clean(data.page)
    ];

    appendRow(row);
    notifyOffice(data, received);
    confirmToSender(data);

    return json({ status: 'ok', message: 'Enquiry received.' });

  } catch (err) {
    console.error(err);
    return json({ status: 'error', message: 'Something went wrong on our end.' });
  }
}

/** Lets you open the web-app URL in a browser to confirm it deployed. */
function doGet() {
  return json({ status: 'ok', message: BUSINESS + ' enquiry endpoint is live.' });
}

// ---------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------

function clean(value) {
  return String(value == null ? '' : value).trim().slice(0, 4000);
}

function json(payload) {
  return ContentService
    .createTextOutput(JSON.stringify(payload))
    .setMimeType(ContentService.MimeType.JSON);
}

function appendRow(row) {
  const book = SpreadsheetApp.openById(SHEET_ID);
  let sheet = book.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = book.insertSheet(SHEET_NAME);
  }
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(COLUMNS);
    sheet.getRange(1, 1, 1, COLUMNS.length)
      .setFontWeight('bold')
      .setBackground('#102c27')
      .setFontColor('#fffefa');
    sheet.setFrozenRows(1);
  }
  sheet.appendRow(row);
}

function notifyOffice(data, received) {
  const type = data.enquiry_type || 'General enquiry';
  const subject = '[' + type + '] ' + clean(data.name) +
    (data.company ? ' — ' + clean(data.company) : '');

  const lines = [
    'New website enquiry — ' + BUSINESS,
    '',
    'Type:        ' + type,
    'Name:        ' + clean(data.name),
    'Company:     ' + (clean(data.company) || '—'),
    'Email:       ' + clean(data.email),
    'Phone:       ' + (clean(data.phone) || '—'),
    'Trade/role:  ' + (clean(data.trade) || '—'),
    'Site suburb: ' + (clean(data.suburb) || '—'),
    'Start date:  ' + (clean(data.start_date) || '—'),
    'Duration:    ' + (clean(data.duration) || '—'),
    '',
    'Details:',
    clean(data.message),
    '',
    '---',
    'Received: ' + Utilities.formatDate(received, 'Australia/Adelaide', 'EEE d MMM yyyy, h:mm a'),
    'Page:     ' + (clean(data.page) || '/')
  ];

  MailApp.sendEmail({
    to: NOTIFY_TO,
    replyTo: clean(data.email),
    subject: subject,
    body: lines.join('\n')
  });
}

function confirmToSender(data) {
  const body = [
    'Hi ' + clean(data.name).split(' ')[0] + ',',
    '',
    'Thanks for getting in touch with ' + BUSINESS + '. Your enquiry has come',
    'through and someone will be back to you by email.',
    '',
    'For your records, this is what you sent:',
    '',
    clean(data.message),
    '',
    '—',
    BUSINESS + ' Pty Ltd',
    '61 Stony Brook Way, Truganina VIC 3029',
    'admin@novaconstructions.com.au',
    '',
    'This email is a confirmation of receipt only. It is not an offer, quote or',
    'acceptance of work, and does not create any agreement between us. Services',
    'are supplied under a separate written agreement.'
  ].join('\n');

  MailApp.sendEmail({
    to: clean(data.email),
    subject: 'We received your enquiry — ' + BUSINESS,
    body: body,
    name: BUSINESS
  });
}
