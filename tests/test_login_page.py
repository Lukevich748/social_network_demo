import allure
import pytest
from allure_commons.types import Severity
from base.base_test import BaseTest


@allure.epic("User Authentication")
class TestLoginPage(BaseTest):

    @pytest.mark.smoke
    @allure.severity(Severity.CRITICAL)
    @allure.feature("Login Functionality")
    @allure.story("Successful Login with Valid Credentials")
    @pytest.mark.parametrize(
        "role", [
            "user",
            "admin"
        ]
    )
    def test_successful_login(self, role):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(role=f"{role}")
        self.news_feed_page().is_opened()