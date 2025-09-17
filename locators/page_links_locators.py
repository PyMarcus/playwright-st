import playwright.sync_api


def options(page: playwright.sync_api.Page) -> None:
    page.goto("https://demo.automationtesting.in/Selectable.html")

    print(f"listing all cookies: {page.context.cookies()}")

    switch_to = page.wait_for_selector('//a[text()="SwitchTo"]')
    switch_to.hover()

    # page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()

    alerts = page.wait_for_selector('//a[text()="Frames"]')
    alerts.click()
