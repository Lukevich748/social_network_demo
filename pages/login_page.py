import os.path
import pickle
import allure
from base.base_page import BasePage
from data.links import Links


class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE

    _USER_NAME_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _LOGIN_BUTTON = "//input[@value='Login']"

    @allure.step("Successful Login into Account")
    def login_as(self, user_name, password):
        if os.path.exists("cookies.pkl"):
            self.driver.delete_all_cookies()

            with open("cookies.pkl", "rb") as cookies_file:
                cookies = pickle.load(cookies_file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.refresh()
        else:
            self.enter_user_name(user_name)
            self.enter_password(password)
            self.click_login_button()
            with open("cookies.pkl", "wb") as cookies_file:
                pickle.dump(self.driver.get_cookies(), cookies_file)

    @allure.step("Enter user name")
    def enter_user_name(self, user_name):
        self.wait_element_to_be_clickable(self._USER_NAME_FIELD)
        self.find(self._USER_NAME_FIELD).clear()
        self.fill(self._USER_NAME_FIELD, user_name)
        assert user_name == self.find(self._USER_NAME_FIELD).get_attribute("value"), f"The user name field does not contain '{user_name}'"

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait_element_to_be_clickable(self._PASSWORD_FIELD)
        self.find(self._PASSWORD_FIELD).clear()
        self.fill(self._PASSWORD_FIELD, password)
        assert password == self.find(self._PASSWORD_FIELD).get_attribute("value"), f"The password field does not contain '{password}'"

    @allure.step("Click on 'Login' button")
    def click_login_button(self):
        self.wait_element_to_be_clickable(self._LOGIN_BUTTON)
        self.click(self._LOGIN_BUTTON)
        assert self.wait_url_to_be(Links.HOME_PAGE, message="The URL did not change to the expected")