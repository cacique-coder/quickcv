const puppeteer = require('puppeteer-core');
const path = require('path');

const input = process.argv[2];
const output = process.argv[3];

if (!input || !output) {
  console.error('Usage: node generate_pdf.js <input.html> <output.pdf>');
  process.exit(1);
}

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/chromium',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-gpu',
      '--disable-dev-shm-usage',
      '--crash-dumps-dir=/tmp',
      '--disable-crash-reporter',
      '--user-data-dir=/tmp/chromium-profile',
    ],
  });

  const page = await browser.newPage();
  const filePath = path.resolve(input);
  await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0' });

  await page.pdf({
    path: output,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
  });

  await browser.close();
  console.log(`PDF generated: ${output}`);
})();
