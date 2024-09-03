import allure
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class BasePage(UIHelper, metaclass=MetaLocator):

    _NEWS_FEED_LINK = "//li[text()='News Feed']"

    @allure.step("Open News Feed Page")
    def open_news_feed_page(self):
        self.click(self._NEWS_FEED_LINK)