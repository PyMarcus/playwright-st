import playwright.sync_api


class UpDown:
    def __init__(self, file: str, path: str) -> None:
        self._file = file
        self._path = path

    def upload(self, page: playwright.sync_api.Page) -> None:
        page.goto("https://demo.automationtesting.in/FileUpload.html")

        uploader = page.wait_for_selector('//input[@type="file"]')


        if uploader:
            uploader.set_input_files(self._file)

            page.wait_for_selector('//button[@type="submit"]').click()
            print(f"File uploaded successfully")