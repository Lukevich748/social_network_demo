import allure
from helpers.ui_helper import UIHelper


class LinksDropdown(UIHelper):

    _NEWS_FEED_LINK = ("xpath", "//li[text()='News Feed']")
    _MESSAGES_LINK = ("xpath", "//li[text()='Messages']")

    @allure.step("Open News Feed Page")
    def open_news_feed_page(self):
        self.click(self._NEWS_FEED_LINK)

    @allure.step("Open Messages Page")
    def open_messages_page(self):
        self.click(self._MESSAGES_LINK)