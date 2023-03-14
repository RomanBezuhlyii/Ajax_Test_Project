from .page import Page


class LoginPage(Page):

    def login(self, login, password):
        """Вхід користувача у свій аккаунт в додатку"""
        self.click_element("//*[@resource-id='com.ajaxsystems:id/login']")
        self.send_keys_to_element("//*[@resource-id='com.ajaxsystems:id/login']", login)
        self.send_keys_to_element("//*[@resource-id='com.ajaxsystems:id/password']", password)
        self.click_element("//*[@resource-id='com.ajaxsystems:id/next']")
