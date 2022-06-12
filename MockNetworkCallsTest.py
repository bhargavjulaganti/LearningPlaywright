import json
from playwright.sync_api import sync_playwright

myList = [
    {
        "book_name": "book from playwright script",
        "isbn": "RSU",
        "aisle": "2301"
    }
]

def test_json(response):
    try:
        # print(request.url)
        print(response.json())
    except:
        pass

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.on("response", lambda response: test_json(response))
    page.goto("https://rahulshettyacademy.com/angularAppdemo/")
    page.route("**/GetBook.php?AuthorName=shetty", lambda route: route.fulfill(
    status=200,
    content_type="application/json",
    body=json.dumps(myList)))
    page.click("//a[contains(@href,'library')]")
    page.wait_for_timeout(10000)
    browser.close()

with sync_playwright() as playwright:    
    run(playwright)