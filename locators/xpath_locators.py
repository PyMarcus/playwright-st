import playwright.sync_api


class PageObject:
    def __init__(self, page: playwright.sync_api.Page):
        self._page = page

    def login(self, username: str, password: str) -> None:
        print(self._page.wait_for_selector('//p[contains(@placeholder, Username)]').text_content())
        print(self._page.wait_for_selector('//div[starts-with(@id, app)]').text_content())

        print([link.get_attribute("href") for link in self._page.query_selector_all('//a')])

        _username = self._page.wait_for_selector('//input[@name="username"]')
        _username.type(username)

        _password = self._page.wait_for_selector('//input[@name="password"]')
        _password.type(password)

        _btn = self._page.wait_for_selector('//button[@type="submit"]')
        _btn.click()
