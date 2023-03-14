from .login_page import LoginPage


class MenuPage(LoginPage):

    def open_menu(self):
        """Розгортання бічного меню додатку"""
        self.click_element("//*[@resource-id='com.ajaxsystems:id/menuDrawer']")
