from pages.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open_login_page()

    login_page.login_as("standard_user", "secret_sauce")

    assert login_page.is_login_successful() is True
    assert "inventory" in page.url.lower()


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.open_login_page()

    login_page.login_as("standard_user", "wrong_password")

    assert login_page.is_error_visible() is True
    assert "Username and password do not match" in login_page.get_error_text()
