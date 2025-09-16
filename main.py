from playwright.sync_api import sync_playwright
from locators import *
from playwright.sync_api import sync_playwright

from locators import *
from locators.alert_locators import click_alerts
from locators.dropdown_locators import select_dropdown
from locators.windows_handling_locators import page_handler
from locators.xpath_locators import PageObject

if __name__ == '__main__':

    url: str = "https://demo.automationtesting.in"
    url2: str = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    _username: str = "Admin"
    _password: str = "admin123"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            #page.goto(url)

            #type_email_input(page)
            #click_enter_button(page)

            #page.wait_for_timeout(3000)

            #page.goto(url2)

            #type_username_and_password_input("Admin", "admin123", page)
            #click_login_button(page)

            #page_object = PageObject(page)
            #page_object.login(_username, _password)

            #dropdown = select_dropdown(page)

            # click_alerts(page)

            page_handler(page, context)

            page.wait_for_timeout(10000)
    except Exception as e:
        print(f"Error: {e}")
