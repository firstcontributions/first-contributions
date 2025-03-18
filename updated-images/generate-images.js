const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function generateImages() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Generate compare-and-pull.png
  const comparePath = path.join(__dirname, 'compare-and-pull.html');
  await page.goto(`file://${comparePath}`);
  await page.setViewport({ width: 1000, height: 400 });
  await page.screenshot({ path: path.join(__dirname, 'compare-and-pull.png') });
  
  // Generate submit-pull-request.png
  const submitPath = path.join(__dirname, 'submit-pull-request.html');
  await page.goto(`file://${submitPath}`);
  await page.setViewport({ width: 1000, height: 600 });
  await page.screenshot({ path: path.join(__dirname, 'submit-pull-request.png') });
  
  await browser.close();
  
  console.log('Images generated successfully!');
}

generateImages().catch(console.error);
