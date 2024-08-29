import os.path
import pickle
import time

from base.base_page import BasePage
from data.credentials import Credentials
from data.links import Links


class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE

    _USER_NAME_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _LOGIN_BUTTON = "//input[@value='Login']"

    def login_as(self, role="user"):
        if role == "user":
            LOGIN = Credentials.USER_LOGIN
            PASSWORD = Credentials.USER_PASSWORD
            cookies_file = "cookies/cookies-user.pkl"
        elif role == "admin":
            LOGIN = Credentials.ADMIN_LOGIN
            PASSWORD = Credentials.ADMIN_PASSWORD
            cookies_file = "cookies/cookies-admin.pkl"

        if os.path.exists(cookies_file):
            self.driver.delete_all_cookies()
            with open(cookies_file, "rb") as cookies_file:
                cookies = pickle.load(cookies_file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.refresh()
        else:
            self.wait_element_to_be_clickable(self._USER_NAME_FIELD)
            self.find(self._USER_NAME_FIELD).clear()
            self.fill(self._USER_NAME_FIELD, LOGIN)
            assert LOGIN == self.find(self._USER_NAME_FIELD).get_attribute("value"), f"The user name field does not contain '{LOGIN}'"

            self.wait_element_to_be_clickable(self._PASSWORD_FIELD)
            self.find(self._PASSWORD_FIELD).clear()
            self.fill(self._PASSWORD_FIELD, PASSWORD)
            assert PASSWORD == self.find(self._PASSWORD_FIELD).get_attribute("value"), f"The password field does not contain '{PASSWORD}'"

            self.wait_element_to_be_clickable(self._LOGIN_BUTTON)
            self.click(self._LOGIN_BUTTON)
            assert self.wait_url_to_be(Links.HOME_PAGE, "The URL did not change to the expected")
            with open(cookies_file, "wb") as cookies_file:
                pickle.dump(self.driver.get_cookies(), cookies_file)