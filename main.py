from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name=" Products").click()
    page.get_by_role("link", name=" Home").click()
    try:
        expect(page.locator("iframe[name=\"aswift_5\"]").content_frame.get_by_role("button", name="Close ad")).to_be_visible()
        page.locator("iframe[name=\"aswift_5\"]").content_frame.get_by_role("button", name="Close ad").click()
    except:
        pass

    # --------------------- #
    
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
