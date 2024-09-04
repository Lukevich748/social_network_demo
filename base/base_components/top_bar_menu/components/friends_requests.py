import allure
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class FriendsRequests(UIHelper, metaclass=MetaLocator):

    _REQUESTS_LIST = "//div[@class='notification-friends']"
    _ITEM_TEXT = ".//a"
    _ITEM_CONFIRM_BUTTON = ".//input[@value='Confirm']"

    def is_friend_request_got(self, friend_name):
        with allure.step(f"Check Receipt of Friend Request From '{friend_name}'"):
            requests_items = self.find_all(self._REQUESTS_LIST)
            for item in requests_items:
                item = item.find_element(*self._ITEM_TEXT)
                if friend_name == item.text:
                    return True
            raise AssertionError("Request was not received.")