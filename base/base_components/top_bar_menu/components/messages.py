import allure
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class Messages(UIHelper, metaclass=MetaLocator):

    _INBOX_MESSAGES_LIST = "//div[@class='user-item message-new']"
    _FRIEND_FULL_NAME = ".//div[@class='name']"
    _INBOX_MESSAGE_TEXT = ".//div[@class='reply-text-from']"

    @property
    def _inbox_messages_list(self):
        return self.find_all(self._INBOX_MESSAGES_LIST)

    def get_inbox_message_by_name(self, friend_name: str):
        for inbox_message in self._inbox_messages_list:
            item = inbox_message.find_element(*self._FRIEND_FULL_NAME)
            if friend_name == item.text:
                return inbox_message
        raise AssertionError(f"Message from '{friend_name}' was not found.")

    def is_inbox_message_received_from(self, friend_name: str, message_text: str):
        with allure.step(f"Check Received a Message From '{friend_name}'"):
            inbox_message = self.get_inbox_message_by_name(friend_name)
            item = inbox_message.find_element(*self._INBOX_MESSAGE_TEXT)
            if message_text == item.text:
                return True
        raise AssertionError("Message was not received.")