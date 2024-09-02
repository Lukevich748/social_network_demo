import allure
import pytest
from faker import Faker
from allure_commons.types import Severity
from base.base_test import BaseTest
from data.credentials import Credentials

fake = Faker()


@allure.epic("User Content Management")
class TestNewsFeedPage(BaseTest):

    @pytest.mark.smoker
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Post Management")
    @allure.story("Create a New Post")
    def test_create_new_post(self):
        post_text = fake.text(max_nb_chars=100)

        self.login_page().open()
        self.login_page().is_opened()
        # self.login_page().login_as(Credentials.USER_LOGIN, Credentials.USER_PASSWORD)
        # self.news_feed_page().is_opened()
        # self.news_feed_page().enter_post_text(post_text)
        # self.news_feed_page().click_post_button()
        # self.news_feed_page().is_post_created(post_text)
