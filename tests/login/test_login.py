import pytest
import account_data as account


@pytest.mark.success_login_test
@pytest.mark.parametrize("login,password", [(account.login, account.password)])
def test_user_login(user_login_fixture, login, password):
    """Тестування успішного входу користувача в додаток"""
    login_page = user_login_fixture
    login_page.login(login, password)
    assert login_page.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/hubAdd']")


@pytest.mark.incorrect_login_data_test
@pytest.mark.parametrize("login,password", [(account.login, 'qa_test_task_password'),
                                            ('test_login@gmail.com', account.password)])
def test_incorrect_user_data(user_login_fixture, login, password):
    """Тестування входу користувача з неправильним логіном або паролем"""
    login_page = user_login_fixture
    login_page.login(login, password)
    assert login_page.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/snackbar_text']").text == "Невірний логін або пароль"


@pytest.mark.incorrect_login_data_test
@pytest.mark.parametrize("login,password", [('', account.password),
                                            (account.login, ''),
                                            ('', '')])
def test_user_missing_field(user_login_fixture, login, password):
    """Тестування входу користувача без заповнення одного з обов'ящкових полів"""
    login_page = user_login_fixture
    login_page.login(login, password)
    assert login_page.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/snackbar_text']").text == "Будь ласка, заповніть усі поля"


@pytest.mark.incorrect_login_data_test
@pytest.mark.parametrize("login,password", [('test_login', account.password),
                                            ('test_login@gmail', account.password),
                                            ('test _login@gmail.com', account.password)])
def test_user_incorrect_email_format(user_login_fixture, login, password):
    """Тестування входу користувача з поштою невірного формату"""
    login_page = user_login_fixture
    login_page.login(login, password)
    assert login_page.find_element_by_xpath("//*[@resource-id='com.ajaxsystems:id/snackbar_text']").text == "Невірний формат електронної пошти"
