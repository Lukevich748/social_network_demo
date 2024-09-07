import allure
import pytest
from faker import Faker
from allure_commons.types import Severity
from base.base_test import BaseTest
from data.credentials import Credentials

fake = Faker()


@allure.epic("Friend's Interaction Management")
class TestFriendsPage(BaseTest):

    @pytest.mark.smoker
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Send Message to Friend")
    @allure.story("Send a message to a Friend from the Friend's Profile")
    # @pytest.mark.parametrize("add_users", [1], indirect=True)
    def test_send_message_to_friend(self):

        # admin = add_users

        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(Credentials.ADMIN_LOGIN, Credentials.ADMIN_PASSWORD)
        self.news_feed_page().is_opened()
        self.news_feed_page().links_dropdown.open_friends_page()
        self.friends_page().is_opened_user_admin(role="admin")
        self.friends_page().open_friends_profile(friend_name="Artem Lukevich")
        self.friends_page().is_friends_profile_opened(friend_name="Artem Lukevich")