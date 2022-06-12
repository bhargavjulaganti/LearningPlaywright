from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    page.wait_for_timeout(5000)
    print(page.title())
    
    browser.close()