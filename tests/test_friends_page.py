import allure
import pytest
from faker import Faker
from allure_commons.types import Severity
from base.base_test import BaseTest

fake = Faker()


@allure.epic("Friend's Interaction Management")
class TestFriendsPage(BaseTest):

    @pytest.mark.smoker
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Send Message to Friend")
    @allure.story("Send a Message to a Friend from the Friend's Profile")
    @pytest.mark.parametrize("add_users", [1], indirect=True)
    def test_send_message_to_friend(self, add_users):
        message_text = fake.text(max_nb_chars=20)

        admin = add_users[0]

        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(role="user")
        self.news_feed_page().is_opened()
        self.news_feed_page().links_dropdown.open_friends_page()
        self.friends_page().is_opened_user_admin()
        self.friends_page().open_friends_profile(friend_name="Administrator")
        self.friends_page().is_friends_profile_opened(friend_name="Administrator")
        self.friends_page().click_message_button()
        self.friends_page().enter_message_text(message_text)
        self.friends_page().click_send_button()
        self.friends_page().is_message_sent(message_text)

        self.login_page(admin).open()
        self.login_page(admin).is_opened()
        self.login_page(admin).login_as(role="admin")
        self.news_feed_page(admin).is_opened()
        self.news_feed_page(admin).top_bar_menu.open_messages()
        self.news_feed_page(admin).top_bar_menu.messages.is_inbox_message_received_from(friend_name="Artem Lukevich", message_text=message_text)