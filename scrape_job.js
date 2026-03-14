const puppeteer = require('puppeteer-core');

const url = process.argv[2];
const outputFile = process.argv[3];

if (!url || !outputFile) {
  console.error('Usage: node scrape_job.js <url> <output.txt>');
  process.exit(1);
}

// Job board-specific selectors for main content containers
const JOB_SELECTORS = [
  // Seek
  '[data-automation="jobDescription"]',
  // Indeed
  '#jobDescriptionText',
  '.jobsearch-jobDescriptionText',
  '.description',
  // LinkedIn
  '.show-more-less-html__markup',
  '.jobs-description__content',
  // Generic
  '[class*="job-description"]',
  '[class*="jobDescription"]',
  '[id*="job-description"]',
  '[id*="jobDescription"]',
  'article',
  'main',
  '[role="main"]',
];

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

  await page.setUserAgent(
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
  );

  // Seek URLs with jobId param need to be converted to direct job URLs
  let targetUrl = url;
  const seekJobIdMatch = url.match(/seek\.com\.au.*[?&]jobId=(\d+)/);
  if (seekJobIdMatch) {
    targetUrl = `https://www.seek.com.au/job/${seekJobIdMatch[1]}`;
  }

  try {
    await page.goto(targetUrl, { waitUntil: 'networkidle2', timeout: 15000 });
  } catch (e) {
    // networkidle2 may time out on some SPAs — proceed with what loaded
    console.error('Navigation warning (proceeding):', e.message);
  }

  // Wait for content, then click "Show more" / "Read more" buttons if present
  await new Promise((resolve) => setTimeout(resolve, 2000));

  // Expand truncated content (common on Seek, Indeed, LinkedIn)
  try {
    await page.evaluate(() => {
      const expandButtons = document.querySelectorAll(
        '[data-automation="showMore"], .show-more-less-html__button, ' +
        'button[aria-label*="Show more"], button[aria-label*="Read more"], ' +
        '.jobsearch-ViewJobButtons-show-more, .view-more-button'
      );
      expandButtons.forEach(btn => btn.click());
    });
    // Wait for expanded content to render
    await new Promise((resolve) => setTimeout(resolve, 1500));
  } catch (e) {
    // No expand button — content is already fully visible
  }

  const result = await page.evaluate((selectors) => {
    function clean(text) {
      return text
        .replace(/\r\n/g, '\n')
        .replace(/\r/g, '\n')
        .replace(/\t/g, ' ')
        .replace(/[ \t]+/g, ' ')           // collapse inline whitespace
        .replace(/\n{3,}/g, '\n\n')        // collapse multiple blank lines
        .trim();
    }

    // Try job-board-specific selectors first
    let bodyText = '';
    for (const sel of selectors) {
      const el = document.querySelector(sel);
      if (el && el.innerText && el.innerText.trim().length > 200) {
        bodyText = el.innerText;
        break;
      }
    }

    // Fall back to full body
    if (!bodyText) {
      bodyText = document.body.innerText || '';
    }

    // Extract useful metadata
    const title = document.title || '';
    const h1 = document.querySelector('h1');
    const jobTitle = h1 ? h1.innerText.trim() : '';

    return {
      text: clean(bodyText),
      title: title,
      jobTitle: jobTitle,
    };
  }, JOB_SELECTORS);

  const fs = require('fs');
  const output = [
    result.jobTitle ? `Job Title: ${result.jobTitle}` : '',
    result.title ? `Page: ${result.title}` : '',
    '',
    result.text,
  ].filter((line, idx) => idx >= 2 || line).join('\n').trim();

  fs.writeFileSync(outputFile, output, 'utf8');
  console.log(`Scraped: ${outputFile}`);

  await browser.close();
})();
