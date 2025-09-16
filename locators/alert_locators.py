import playwright.sync_api


def click_alerts(page: playwright.sync_api.Page) -> None:
    page.goto("https://demo.automationtesting.in/Alerts.html")

    button = page.wait_for_selector('//button[@class="btn btn-danger"]')

    page.on("dialog", lambda dialog: print("Mensagem do alert:", dialog.message) or dialog.accept())

    button.click()
    # page.wait_for_timeout(10000)
