from playwright.async_api import async_playwright

async def scan_page(url):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)

        page = await browser.new_page()

        response =await page.goto(url)

        final_url = page.url

        status = response.status

        title = await page.title()

        await browser.close()

        return {
            "url": url,
            "title":title,
            "finalurl": final_url,
            "status": status
        }