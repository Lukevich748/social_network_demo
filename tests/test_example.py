import time

from base.base_test import BaseTest


class TestExample(BaseTest):

    def test_example(self):
        self.login_page.open()
        self.login_page.login_as("admin")