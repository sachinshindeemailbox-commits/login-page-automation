from pages.base_page import BasePage


class LoginPage(BasePage):
    url = "https://www.saucedemo.com/"

    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    error_message = "[data-test='error']"
    inventory_container = ".inventory_container"

    def open_login_page(self):
        self.open(self.url)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def enter_username(self, username: str):
        self.page.fill(self.username_input, username)

    def enter_password(self, password: str):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def login_as(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_error_visible(self) -> bool:
        return self.page.is_visible(self.error_message)

    def is_login_successful(self) -> bool:
        return self.page.is_visible(self.inventory_container)

    def get_error_text(self) -> str:
        return self.page.locator(self.error_message).text_content().strip()
