import allure
import pytest
from faker import Faker
from allure_commons.types import Severity
from base.base_test import BaseTest

fake = Faker()


@allure.epic("User Content Management")
class TestNewsFeedPage(BaseTest):

    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Post Management")
    @allure.story("Create a New Post")
    def test_create_new_post(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(role="user")
        self.news_feed_page().is_opened()
        self.news_feed_page().enter_post_text(post_text=self.post_text)
        self.news_feed_page().click_post_button()
        post_id = self.news_feed_page().get_post_id()
        self.news_feed_page().is_post_created(post_id)

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=2, reruns_delay=2, max_reruns=2)
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Post Management")
    @allure.story("Edit a Post")
    def test_edit_post(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(role="user")
        self.news_feed_page().is_opened()
        self.news_feed_page().enter_post_text(post_text=self.post_text)
        self.news_feed_page().click_post_button()
        post_id = self.news_feed_page().get_post_id()
        self.news_feed_page().is_post_created(post_id=post_id)
        self.news_feed_page().edit_post(new_post_text=self.new_post_text, post_id=post_id)
        self.news_feed_page().is_post_edited(new_post_text=self.new_post_text, post_id=post_id)

    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Post Management")
    @allure.story("Delete a Post")
    def test_delete_post(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(role="user")
        self.news_feed_page().is_opened()
        self.news_feed_page().enter_post_text(post_text=self.post_text)
        self.news_feed_page().click_post_button()
        post_id = self.news_feed_page().get_post_id()
        self.news_feed_page().is_post_created(post_id)
        self.news_feed_page().delete_post(post_id=post_id)
        self.news_feed_page().is_post_deleted(post_id=post_id)