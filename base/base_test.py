from pages.home_page import HomePage
from pages.login_page import LoginPage


class BaseTest:

    def setup_method(self):
        self.login_page = lambda driver=self.driver: LoginPage(driver)
        self.home_page = lambda driver=self.driver: HomePage(driver)