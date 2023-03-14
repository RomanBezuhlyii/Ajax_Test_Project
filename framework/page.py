from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def find_element_by_xpath(self, xpath):
        """Пошук елементів сторінки за допомогою xpath"""
        return self.driver.find_element(AppiumBy.XPATH, value=xpath)

    def check_element_on_page(self, xpath):
        """Перевірка наявності елементу на сторінці"""
        try:
            self.find_element_by_xpath(xpath)
        except:
            return False
        else:
            return True

    def click_element(self, xpath):
        """Клік по елементу після його знаходження"""
        self.find_element_by_xpath(xpath).click()

    def click_element_with_offset(self, xpath, offset_x, offset_y):
        element = self.find_element_by_xpath(xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, offset_x, offset_y)
        actions.click()
        actions.perform()

    def wait_element(self, xpath):
        """Очікування появи необхідного елементу"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((AppiumBy.XPATH, xpath)))
        return self.find_element_by_xpath(xpath)

    def send_keys_to_element(self, xpath, data):
        """Відправлення набору символів до елементу"""
        element = self.wait_element(xpath)
        self.click_element(xpath)
        element.send_keys(data)

    def reset_app(self):
        """Скидання і перезапуск запущенного додатку"""
        self.driver.reset()

    def go_back(self):
        """Реалізує команду 'Назад'"""
        self.driver.back()
