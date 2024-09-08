import allure
import pytest
from faker import Faker
from allure_commons.types import Severity
from base.base_test import BaseTest

fake = Faker()


@allure.epic("User Social Interaction")
class TestBasePage(BaseTest):

    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Friend Management")
    @allure.story("Add User to Friends List")
    @pytest.mark.parametrize("add_users", [1], indirect=True)
    def test_add_user_to_friends_list(self, add_users):

        admin = add_users[0]

        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(role="user")
        self.news_feed_page().is_opened()
        self.news_feed_page().send_friend_request_to(friend_name="Admin")
        self.news_feed_page().is_friend_request_sent()

        self.login_page(admin).open()
        self.login_page(admin).is_opened()
        self.login_page(admin).login_as(role="admin")
        self.news_feed_page(admin).is_opened()
        self.news_feed_page(admin).top_bar_menu.open_friend_requests()
        self.news_feed_page(admin).top_bar_menu.friends_requests.is_friend_request_received_from(friend_name="Artem Lukevich")
        self.news_feed_page(admin).top_bar_menu.friends_requests.click_confirm_button(friend_name="Artem Lukevich")