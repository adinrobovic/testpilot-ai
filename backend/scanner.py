from playwright.async_api import async_playwright
import os
import uuid

async def scan_page(url):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)

        page = await browser.new_page()

        console_errors = []

        def handle_console(msg):
            if msg.type == "error":
                console_errors.append(msg.text)

        page.on("console", handle_console)

        failed_requests = []

        def handle_failed_request(request):
            failed_requests.append({
                "url": request.url,
                "failure":request.failure
            })

        page.on("requestfailed", handle_failed_request)

        bad_responses = []

        def handle_response(response):
            if response.status >= 400:
                bad_responses.append({
                    "url": response.url,
                    "status": response.status
                })

        page.on("response", handle_response)

        response =await page.goto(url)

        final_url = page.url

        status = response.status

        title = await page.title()

        screenshot_path = f"screenshots/{uuid.uuid4()}.png"
        
        await page.screenshot(
            path=screenshot_path,
            full_page=True
        )

        await browser.close()

        return {
            "url": url,
            "title":title,
            "finalurl": final_url,
            "status": status,
            "screenshot": screenshot_path,
            "console_errors": console_errors,
            "failed_requests": failed_requests,
            "bad_responses": bad_responses
        }

    