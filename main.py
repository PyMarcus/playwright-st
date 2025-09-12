from playwright.sync_api import sync_playwright
from locators import *


if __name__ == '__main__':

    url: str = "https://demo.automationtesting.in"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        type_email_input(page)
        click_enter_button(page)

        page.wait_for_timeout(10000)
