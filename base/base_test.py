from pages.friends_page import FriendsPage
from pages.news_feed_page import NewsFeedPage
from pages.login_page import LoginPage
from pages.messages_page import MessagesPage


class BaseTest:

    def setup_method(self):
        self.login_page = lambda driver=self.driver: LoginPage(driver)
        self.news_feed_page = lambda driver=self.driver: NewsFeedPage(driver)
        self.friends_page = lambda driver=self.driver: FriendsPage(driver)
        self.messages_page = lambda driver=self.driver: MessagesPage(driver)