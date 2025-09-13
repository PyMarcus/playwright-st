from playwright.sync_api import sync_playwright
from locators import *
from playwright.sync_api import sync_playwright

from locators import *

if __name__ == '__main__':

    url: str = "https://demo.automationtesting.in"
    url2: str = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(url)

            type_email_input(page)
            click_enter_button(page)

            page.wait_for_timeout(3000)

            page.goto(url2)

            type_username_and_password_input("Admin", "admin123", page)
            click_login_button(page)

            page.wait_for_timeout(10000)
    except Exception as e:
        print(f"Error: {e}")
