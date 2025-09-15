import playwright.sync_api
from playwright.sync_api import sync_playwright


def select_dropdown(page: playwright.sync_api.Page) -> None:
    page.goto("https://demo.automationtesting.in/Register.html")

    selected_dropdown = page.query_selector('//select[@id="Skills"]')
    selected_dropdown.select_option(label="Art Design")


