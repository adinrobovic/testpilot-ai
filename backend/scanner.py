from playwright.async_api import async_playwright
import os
import uuid
from axe_playwright_python.async_playwright import Axe

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

        axe = Axe()
        axe_results = await axe.run(page)

        accessibility_violations = axe_results.response["violations"]

        accessibility_findings = []

        for violation in accessibility_violations:
            accessibility_findings.append({
                "id":violation["id"],
                "severity":violation["impact"],
                "title":violation["help"],
                "businessImpact": "",
                "affectedPage":page.url,
                "technicalDetails":violation["description"],
                "helpUrl":violation["helpUrl"],
                "nodes":violation["nodes"]
            })

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
            "bad_responses": bad_responses,
            "accessibility_violation_count": axe_results.violations_count,
            "accessibility_violations": accessibility_violations,
            "accessibility_findgins": accessibility_findings
        }

    