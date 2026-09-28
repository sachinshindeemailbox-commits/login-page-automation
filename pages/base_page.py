from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")

    def get_title(self) -> str:
        return self.page.title()
