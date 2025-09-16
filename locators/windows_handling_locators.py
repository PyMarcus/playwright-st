import playwright.sync_api


def page_handler(page: playwright.sync_api.Page, context: playwright.sync_api.BrowserContext) -> None:
    page.goto("https://demo.automationtesting.in/Windows.html")

    page.wait_for_selector('//button[@class="btn btn-info"]').click()
    page.wait_for_timeout(3000)
    pages = context.pages
    print(f"Total pages: {len(pages)}")
    for i, site in enumerate(pages):
        print(f"Link {i + 1}) {site}")

    print(f"Title page 1: {pages[0].title()}")
    page_2 = pages[1]
    page_2.bring_to_front()
    print(f"Title page 2: {page_2.title()}")

    page.wait_for_timeout(3000)
    pages[0].bring_to_front()
    page.wait_for_timeout(5000)

    page_2.close()