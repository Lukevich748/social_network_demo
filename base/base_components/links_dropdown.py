import allure
from helpers.ui_helper import UIHelper


class LinksDropdown(UIHelper):

    _NEWS_FEED_LINK = "//li[text()='News Feed']"
    _MESSAGES_LINK = "//li[text()='Messages']"
    _FRIENDS_LINK = "//li[text()='Friends']"

    @allure.step("Open 'News Feed Page'")
    def open_news_feed_page(self):
        self.click(self._NEWS_FEED_LINK)

    @allure.step("Open 'Messages Page'")
    def open_messages_page(self):
        self.click(self._MESSAGES_LINK)

    @allure.step("Open 'Friends Page'")
    def open_friends_page(self):
        self.click(self._FRIENDS_LINK)