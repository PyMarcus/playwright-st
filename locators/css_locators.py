import playwright.sync_api


def type_email_input(page: playwright.sync_api.Page) -> None:
    input_email_txt = page.query_selector("#email")
    input_email_txt.type("marcus-test@email.com")


def click_enter_button(page: playwright.sync_api.Page) -> None:
    button = page.query_selector("#enterimg")
    button.click()
