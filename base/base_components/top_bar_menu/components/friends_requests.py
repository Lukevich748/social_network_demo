import allure
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class FriendsRequests(UIHelper, metaclass=MetaLocator):

    _REQUESTS_LIST = "//div[@class='notification-friends']"
    _ITEM_TEXT = ".//a"
    _ITEM_CONFIRM_BUTTON = ".//input[@value='Confirm']"

    @property
    def _requests_items(self):
        return self.find_all(self._REQUESTS_LIST)

    def get_item_by_name(self, friend_name):
        for request_item in self._requests_items:
            item = request_item.find_element(*self._ITEM_TEXT)
            if friend_name == item.text:
                return request_item
        raise AssertionError(f"Request from '{friend_name}' was not found")

    def is_friend_request_got(self, friend_name):
        with allure.step(f"Check Received a Friend Request From '{friend_name}'"):
            if self.get_item_by_name(friend_name):
                return True
        raise AssertionError("Request was not received.")

    @allure.step("Click 'Confirm' Button")
    def click_confirm_button(self, friend_name):
        request_item = self.get_item_by_name(friend_name)
        confirm_button = request_item.find_element(*self._ITEM_CONFIRM_BUTTON)
        confirm_button.click()