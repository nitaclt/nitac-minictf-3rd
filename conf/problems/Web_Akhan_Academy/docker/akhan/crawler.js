const puppeteer = require('puppeteer')

const HOST = "http://akhn.ctf.jyoken.net/";

(async () => {
  const browser = await puppeteer.launch({
    args: ['--disable-setuid-sandbox', '--no-sandbox'],
  })

  const page = await browser.newPage()
  await page.goto(`${HOST}/hey-crawler-845104ea3931ff88ab3d5dbb34249ff983b01410c67ac4cd8978ed1802177bbf`)

  await page.goto(`${HOST}/`)
  await page.waitForNavigation({ waitUntil: 'networkidle2' })

  const html = await page.evaluate(() => document.body.innerHTML)
  if (!html.includes("NITAC{")) {
    console.log("Can't see the FLAG! stopping...")
    await browser.close()
    return
  }

  const crawl = async () => {
    console.log("crawling...")
    await page.goto(`${HOST}/`, {waitUntil: 'networkidle2'})
    console.log(await page.evaluate(() => document.cookie))
  };

  setInterval(crawl, 10000)
})()

