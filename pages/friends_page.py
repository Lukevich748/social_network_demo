import time

from selenium.webdriver.remote.webelement import WebElement

from base.base_page import BasePage
from data.links import Links


class FriendsPage(BasePage):

    _PAGE_URL_USER = Links.FRIENDS_PAGE_USER
    _PAGE_URL_ADMIN = Links.FRIENDS_PAGE_ADMIN

    _FRIENDS_TABLE = "//div[@class='module-contents']"
    _FRIENDS_ITEMS = ".//div[@class='row ossn-users-list-item']"
    _ITEM_FRIEND_NAME = ".//div[@class='uinfo']//a"
    item_friend_name_locator = lambda self, friend_name: ("xpath", f"//a[contains(text(), '{friend_name}')]")
    _NEXT_PAGE_BUTTON = "//ul[contains(@class, 'ossn-pagination')]//a[text()='Last']"


    @property
    def _friends_table(self) -> WebElement:
        return self.find(self._FRIENDS_TABLE)

    @property
    def _friends_items(self) -> list[WebElement]:
        friends_table = self._friends_table
        return friends_table.find_elements(*self._FRIENDS_ITEMS)

    def next_page(self) -> WebElement:
        return self.find(self._NEXT_PAGE_BUTTON)

    # def get_friend_item_by_name(self, friend_name: str):
    #     while True:
    #         for friend_item in self._friends_items:
    #             item = friend_item.find_element(*self._ITEM_FRIEND_NAME)
    #             if friend_name in item.text:
    #                 return friend_item
    #         self.next_page()
    #
    def open_friends_profile(self, friend_name):
        for friend_item in self._friends_items:
            item = friend_item.find_element(*self._ITEM_FRIEND_NAME)
            if friend_name in item.text:
                item.click()
        # friend_item = self.get_friend_item_by_name(friend_name)
        # item_user_name = friend_item.find_element(*self._ITEM_FRIEND_NAME)
        # self.scroll_to_element(self.item_friend_name_locator(friend_name))
        # time.sleep(1)
        # item_user_name.click()