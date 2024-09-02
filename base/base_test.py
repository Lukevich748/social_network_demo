from pages.news_feed_page import NewsFeedPage
from pages.login_page import LoginPage


class BaseTest:

    def setup_method(self):
        self.login_page = lambda driver=self.driver: LoginPage(driver)
        self.news_feed_page = lambda driver=self.driver: NewsFeedPage(driver)