import pytest


@pytest.mark.menu_tests
def test_open_add_hub(open_menu_fixture):
    """Тестування переходу по кнопці 'Додати хаб'"""
    menu = open_menu_fixture
    menu.click_element("//*[@resource-id='com.ajaxsystems:id/addHub']")
    assert menu.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/toolbarTitle']").text == "Додати хаб"


@pytest.mark.menu_tests
def test_open_settings(open_menu_fixture):
    """Тестування переходу по кнопці 'Налаштування застосунку'"""
    menu = open_menu_fixture
    menu.click_element("//*[@resource-id='com.ajaxsystems:id/settings']")
    assert menu.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/accountInfoLogoutNavigate']")


@pytest.mark.menu_tests
def test_open_help(open_menu_fixture):
    """Тестування переходу по кнопці 'Допомога'"""
    menu = open_menu_fixture
    menu.click_element("//*[@resource-id='com.ajaxsystems:id/help']")
    assert menu.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/toolbarTitle']").text == 'Інструкції з установки'


@pytest.mark.menu_tests
def test_open_problem_info(open_menu_fixture):
    """Тестування переходу по кнопці 'Повідомити про проблему'"""
    menu = open_menu_fixture
    menu.click_element("//*[@resource-id='com.ajaxsystems:id/logs']")
    assert menu.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/title']").text == 'Повідомити про проблему'


@pytest.mark.menu_tests
def test_open_video_cameras(open_menu_fixture):
    """Тестування переходу по кнопці 'Відеоспостереження'"""
    menu = open_menu_fixture
    menu.click_element("//*[@resource-id='com.ajaxsystems:id/camera']")
    assert menu.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/toolbarTitle']").text == 'Відеоспостереження'


@pytest.mark.menu_tests
def test_open_privacy_politic(open_menu_fixture):
    """Тестування переходу по кнопці 'Умови використання'"""
    menu = open_menu_fixture
    menu.click_element("//*[@resource-id='com.ajaxsystems:id/documentation_text']")
    assert menu.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/toolbarTitle']").text == 'Умови використання'


@pytest.mark.menu_tests
def test_click_outside_menu_area(open_menu_fixture):
    """Тестування кліку на область поза меню"""
    menu = open_menu_fixture
    menu.click_element_with_offset("//*[@resource-id='com.ajaxsystems:id/settings']",500,0)
    assert menu.check_element_on_page("//*[@resource-id='com.ajaxsystems:id/addFirstHub']")


@pytest.mark.menu_tests
def test_click_free_meny_area(open_menu_fixture):
    """Тестування кліку на вільну область в меню"""
    menu = open_menu_fixture
    menu.click_element_with_offset("//*[@resource-id='com.ajaxsystems:id/camera']", 0, 300)
    assert menu.check_element_on_page("//*[@resource-id='com.ajaxsystems:id/camera']")
