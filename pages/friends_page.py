import allure
from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.links import Links


class FriendsPage(BasePage):

    _PAGE_URL_USER = Links.FRIENDS_PAGE_USER
    _PAGE_URL_ADMIN = Links.FRIENDS_PAGE_ADMIN

    _FRIENDS_TABLE = "//div[@class='module-contents']"
    _FRIENDS_LIST = ".//div[@class='row ossn-users-list-item']"
    _ITEM_FRIEND_NAME = ".//div[@class='uinfo']//a"

    _NEXT_PAGE_BUTTON = "//ul[contains(@class, 'ossn-pagination')]//a[text()='Last']"

    _FRIEND_PROFILE_FULL_NAME = "//div[@class='user-fullname']"
    _MESSAGE_BUTTON = "//a[@id='profile-message']"
    _MESSAGE_TEXT_INPUT = "//textarea[@placeholder='Enter text here']"
    _SEND_BUTTON = "//input[@value='Send']"
    _SENT_MESSAGES_LIST = "//div[@class='message-box-sent text']/span"


    @property
    def _friends_table(self) -> WebElement:
        return self.find(self._FRIENDS_TABLE)

    @property
    def _friends_list(self) -> list[WebElement]:
        friends_table = self._friends_table
        return friends_table.find_elements(*self._FRIENDS_LIST)

    def get_friend_item_by_name(self, friend_name: str):
        while True:
            for friend_item in self._friends_list:
                user_link = friend_item.find_element(*self._ITEM_FRIEND_NAME)
                if friend_name in user_link.text:
                    return friend_item
            next_page_button = self.find(self._NEXT_PAGE_BUTTON)
            self.scroll_to_element(next_page_button)
            next_page_button.click()

    def open_friends_profile(self, friend_name):
        with allure.step(f"Open Friend's Profile: '{friend_name}'"):
            friend_item = self.get_friend_item_by_name(friend_name)
            user_link = friend_item.find_element(*self._ITEM_FRIEND_NAME)
            if friend_name in user_link.text:
                self.scroll_to_element(user_link)
                user_link.click()

    def is_friends_profile_opened(self, friend_name):
        with allure.step(f"Check '{friend_name}'s' Profile is Opened"):
            assert friend_name in self.find(self._FRIEND_PROFILE_FULL_NAME).text

    @allure.step("Click 'Message' Button")
    def click_message_button(self):
        self.click(self._MESSAGE_BUTTON)

    @allure.step("Enter Message Text")
    def enter_message_text(self, message_text: str):
        self.wait_element_to_be_clickable(self._MESSAGE_TEXT_INPUT)
        self.find(self._MESSAGE_TEXT_INPUT).clear()
        self.fill(self._MESSAGE_TEXT_INPUT, message_text)
        assert message_text == self.find(self._MESSAGE_TEXT_INPUT).get_attribute("value"), f"The input area does not contain '{message_text}'"

    @allure.step("Click 'Send' Button")
    def click_send_button(self):
        self.click(self._SEND_BUTTON)
        self.wait_element_to_be_clickable(self._SEND_BUTTON)

    @allure.step("Check Send a Message to Friend")
    def is_message_sent(self, message_text: str):
        sent_messages_list = self.find_all(self._SENT_MESSAGES_LIST)
        assert message_text == sent_messages_list[-1].text, "Message was not sent."