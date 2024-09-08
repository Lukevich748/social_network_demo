import allure
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class FriendRequests(UIHelper, metaclass=MetaLocator):

    _FRIEND_REQUESTS_LIST = "//div[@class='notification-friends']"
    _FRIEND_REQUEST_FULL_NAME = ".//a"
    _REQUEST_CONFIRM_BUTTON = ".//input[@value='Confirm']"

    @property
    def _friend_requests_list(self):
        return self.find_all(self._FRIEND_REQUESTS_LIST)

    def get_friend_request_by_name(self, friend_name: str):
        for friend_request in self._friend_requests_list:
            item = friend_request.find_element(*self._FRIEND_REQUEST_FULL_NAME)
            if friend_name == item.text:
                return friend_request
        raise AssertionError(f"Request from '{friend_name}' was not found.")

    def is_friend_request_received_from(self, friend_name: str):
        with allure.step(f"Check Received a Friend Request From '{friend_name}'"):
            if self.get_friend_request_by_name(friend_name):
                return True
        raise AssertionError("Request was not received.")

    @allure.step("Click 'Confirm' Button")
    def click_confirm_button(self, friend_name: str):
        request_item = self.get_friend_request_by_name(friend_name)
        confirm_button = request_item.find_element(*self._REQUEST_CONFIRM_BUTTON)
        self.click(confirm_button)
        self.wait_invisibility_of_element(confirm_button, message="The button 'Confirm' was not clicked.")