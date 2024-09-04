import allure
from selenium.webdriver import Keys
from base.base_components.groups_dropdown import GroupsDropdown
from base.base_components.links_dropdown import LinksDropdown
from base.base_components.top_bar_menu.components.friends_requests import FriendsRequests
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class BasePage(UIHelper, metaclass=MetaLocator):

    # Side Bar Menu
    _LINKS_DROPDOWN = "//div[@class='sidebar-menu']//a[text()='Links']"
    _GROUPS_DROPDOWN = "//div[@class='sidebar-menu']//a[text()='Groups']"

    _SEARCH_INPUT = "//input[@placeholder='Search']"
    _SEARCH_RESULT_CONTENT = "//div[contains(@class, 'newsfeed-middle')]"
    _SEARCH_RESULT_CONTENT_TEXT = "//div[contains(@class, 'newsfeed-middle')]//a[contains(@class, 'output-user')]"

    _ADD_FRIEND_BUTTON = "//a[text()='Add Friend']"
    _CANCEL_REQUEST_BUTTON = "//a[text()='Cancel Request']"
    _SUCCESS_ALERT = "//div[contains(@class, 'alert-success')]"

    _NOTIFICATIONS_COUNT = "//span[@class='ossn-notification-container']"

    def __init__(self, driver):
        super().__init__(driver)
        self.links_dropdown = LinksDropdown(self.driver)
        self.groups_dropdown = GroupsDropdown(self.driver)
        self.top_bar_menu = TopBarMenu(self.driver)

    @allure.step("Open | Close Links Dropdown")
    def click_links_dropdown(self):
        self.click(self._LINKS_DROPDOWN)

    @allure.step("Open | Close Links Dropdown")
    def click_groups_dropdown(self):
        self.click(self._GROUPS_DROPDOWN)

    def send_friend_request_to(self, friend_name):
        with allure.step(f"Send a Friend Request to '{friend_name}'"):
            self.wait_element_to_be_clickable(self._SEARCH_INPUT)
            self.find(self._SEARCH_INPUT).clear()
            self.fill(self._SEARCH_INPUT, friend_name)
            assert friend_name == self.find(self._SEARCH_INPUT).get_attribute("value"), f"The search field does not contain '{friend_name}'."
            self.fill(self._SEARCH_INPUT, Keys.ENTER)

            search_result = self.find(self._SEARCH_RESULT_CONTENT_TEXT)
            assert friend_name in search_result.text, f"User with name '{friend_name}' was not found."
            self.click(self._ADD_FRIEND_BUTTON)

    @allure.step("Check Post Edit")
    def is_friend_request_sent(self):
        self.wait_visibility_of_element(self._CANCEL_REQUEST_BUTTON)
        self.wait_visibility_of_element(self._SUCCESS_ALERT)
        assert "Friend Request Sent" == self.find(self._SUCCESS_ALERT).text, "Request to friend was not sent."


class TopBarMenu(UIHelper, metaclass=MetaLocator):

    # Top Bar Menu
    _FRIEND_REQUESTS_BUTTON = "//li[@id='ossn-notif-friends']"

    def __init__(self, driver):
        super().__init__(driver)
        self.friends_requests = FriendsRequests(self.driver)

    @allure.step("Open | Close Friends Requests Top Bar Menu")
    def click_friend_requests(self):
        self.click(self._FRIEND_REQUESTS_BUTTON)