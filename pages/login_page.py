import os.path
import pickle
import allure
from base.base_page import BasePage
from data.credentials import Credentials
from data.links import Links


class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE

    _USER_NAME_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _LOGIN_BUTTON = "//input[@value='Login']"

    @allure.step("Successful Login into Account")
    def login_as(self, role="user"):
        if role == "admin":
            user_name = Credentials.ADMIN_LOGIN
            password = Credentials.ADMIN_PASSWORD
            cookies_file = "cookies/admin-cookies.pkl"
        else:
            user_name = Credentials.USER_LOGIN
            password = Credentials.USER_PASSWORD
            cookies_file = "cookies/user-cookies.pkl"

        if os.path.exists(cookies_file):
            self.driver.delete_all_cookies()

            with open(cookies_file, "rb") as cookies_file:
                cookies = pickle.load(cookies_file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.refresh()
        else:
            self.enter_user_name(user_name)
            self.enter_password(password)
            self.click_login_button()
            with open(cookies_file, "wb") as cookies_file:
                pickle.dump(self.driver.get_cookies(), cookies_file)

    @allure.step("Enter user name")
    def enter_user_name(self, user_name):
        self.wait_element_to_be_clickable(self._USER_NAME_FIELD)
        self.find(self._USER_NAME_FIELD).clear()
        self.fill(self._USER_NAME_FIELD, user_name)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait_element_to_be_clickable(self._PASSWORD_FIELD)
        self.find(self._PASSWORD_FIELD).clear()
        self.fill(self._PASSWORD_FIELD, password)

    @allure.step("Click on 'Login' button")
    def click_login_button(self):
        self.wait_element_to_be_clickable(self._LOGIN_BUTTON)
        self.click(self._LOGIN_BUTTON)