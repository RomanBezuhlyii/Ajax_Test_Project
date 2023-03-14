import pytest
from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    """Створює екземпляр классу LoginPage та передає його до функцій тестів"""
    login_page = LoginPage(driver)
    yield login_page
    login_page.reset_app()
