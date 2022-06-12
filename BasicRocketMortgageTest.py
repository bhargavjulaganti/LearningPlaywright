from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rocketmortgage.com/")
    page.click("(//*[contains(@href,'https://www.rocketmortgage.com/pre-sign')])[2]")
    page.fill("#username", "bhargavajulaganti@rocketmortgage.com")
    page.fill("#password", "Bh@17037")
    page.click("#sign-in-submit")
    page.wait_for_timeout(5000)
    print(page.title())
    browser.close()