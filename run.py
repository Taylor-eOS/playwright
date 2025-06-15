from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://juliansimon.com')
    text = page.inner_text('body')
    with open('output.txt', 'w') as f:
        f.write(text)
    browser.close()

