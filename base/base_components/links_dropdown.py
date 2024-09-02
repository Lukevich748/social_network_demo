import allure
from helpers.ui_helper import UIHelper
from pages.news_feed_page import NewsFeedPage


class LinksDropdown(UIHelper):

    _NEWS_FEED_LINK = "//li[text()='News Feed']"

    def __init__(self, driver):
        super().__init__(driver)
        self.news_feed_page = NewsFeedPage(self.driver)

    @allure.step("Open News Feed Page")
    def open_news_feed_page(self):
        self.click(self._NEWS_FEED_LINK)