import time

import allure
import pytest
from faker import Faker
from allure_commons.types import Severity
from base.base_test import BaseTest
from data.credentials import Credentials

fake = Faker()


@allure.epic("User Content Management")
class TestNewsFeedPage(BaseTest):

    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Post Management")
    @allure.story("Create a New Post")
    def test_create_new_post(self):
        post_text = fake.text(max_nb_chars=100)

        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(Credentials.USER_LOGIN, Credentials.USER_PASSWORD)
        self.news_feed_page().is_opened()
        self.news_feed_page().enter_post_text(post_text)
        self.news_feed_page().click_post_button()
        self.news_feed_page().is_post_created(post_text)

    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Post Management")
    @allure.story("Edit a Post")
    def test_edit_post(self):
        post_text = fake.text(max_nb_chars=100)
        edited_post_text = fake.text(max_nb_chars=100)

        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(Credentials.USER_LOGIN, Credentials.USER_PASSWORD)
        self.news_feed_page().is_opened()
        self.news_feed_page().enter_post_text(post_text)
        self.news_feed_page().click_post_button()
        self.news_feed_page().is_post_created(post_text)
        self.news_feed_page().edit_post(post_text, edited_post_text)
        self.news_feed_page().is_post_edited(edited_post_text)

    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Post Management")
    @allure.story("Delete a Post")
    def test_delete_post(self):
        post_text = fake.text(max_nb_chars=100)

        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(Credentials.USER_LOGIN, Credentials.USER_PASSWORD)
        self.news_feed_page().is_opened()
        self.news_feed_page().enter_post_text(post_text)
        self.news_feed_page().click_post_button()
        self.news_feed_page().is_post_created(post_text)
        self.news_feed_page().delete_post(post_text)
        self.news_feed_page().is_post_deleted(post_text)