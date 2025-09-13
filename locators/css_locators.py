import playwright.sync_api


def type_email_input(page: playwright.sync_api.Page) -> None:
    input_email_txt = page.query_selector("#email")
    input_email_txt.type("marcus-test@email.com")


def click_enter_button(page: playwright.sync_api.Page) -> None:
    button = page.query_selector("#enterimg")
    button.click()


def type_username_and_password_input(username: str, password: str, page: playwright.sync_api.Page) -> None:
    input_username_txt = page.wait_for_selector('input[name="username"]')
    input_username_txt.type(username)

    input_password_txt = page.wait_for_selector('input[name="password"]')
    input_password_txt.type(password)


def click_login_button(page: playwright.sync_api.Page) -> None:
    input_password_txt = page.wait_for_selector('button[type="submit"]')
    input_password_txt.click()
