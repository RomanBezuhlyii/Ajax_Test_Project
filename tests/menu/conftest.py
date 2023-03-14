import pytest
from framework.menu_page import MenuPage
import account_data as account


@pytest.fixture(scope='module')
def menu_login_fixture(driver):
    """Створює екземпляр классу MenuPage та передає його до функцій тестів"""
    menu_page = MenuPage(driver)
    menu_page.login(account.login, account.password)
    yield menu_page


@pytest.fixture(scope='function')
def open_menu_fixture(menu_login_fixture):
    """Відкриття меню та вихід з нього після тесту"""
    menu_login_fixture.open_menu()
    yield menu_login_fixture
    menu_login_fixture.go_back()
