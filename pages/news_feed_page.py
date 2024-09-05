import allure
from base.base_page import BasePage
from data.links import Links


class NewsFeedPage(BasePage):

    _PAGE_URL = Links.NEWS_FEED_PAGE

    _POST_TEXT_INPUT = "//textarea[@name='post']"
    _POST_BUTTON = "//input[@type='submit']"
    _POSTS_ITEMS_LIST = "//div[@class='user-activity']/div[descendant::a[@data-bs-toggle='dropdown']]"
    _POST_ITEM_CONTENT_TEXT = "//div[@class='user-activity']//div[@class='post-contents']"
    _POST_ITEM_ACTION_DROPDOWN = "//div[@post='new']//a[@data-bs-toggle='dropdown']"
    _POST_ITEM_EDIT_BUTTON = "//div[@post='new']//a[text()='Edit']"
    _POST_ITEM_DELETE_BUTTON = "//div[@post='new']//a[text()='Delete']"

    _POST_EDIT_SAVE_BUTTON = "//div[@class='control']//a[text()='Save']"
    _POST_EDIT_TEXT_INPUT = "//textarea[@id='post-edit']"

    # Posts
    @allure.step("Enter Post Text")
    def enter_post_text(self, post_text: str):
        self.wait_element_to_be_clickable(self._POST_TEXT_INPUT)
        self.find(self._POST_TEXT_INPUT).clear()
        self.fill(self._POST_TEXT_INPUT, post_text)
        assert post_text == self.find(self._POST_TEXT_INPUT).get_attribute("value"), f"The input area does not contain '{post_text}'"

    @allure.step("Click Post Button")
    def click_post_button(self):
        self.click(self._POST_BUTTON)
        self.wait_element_to_be_clickable(self._POST_BUTTON)

    @allure.step("Check Post Created")
    def is_post_created(self, post_text: str):
        posts_text_list = self.find_all(self._POST_ITEM_CONTENT_TEXT)
        for post in posts_text_list:
            if post_text in post.text:
                return True
        raise AssertionError("Post was not created.")

    @allure.step("Delete a Post")
    def delete_post(self, post_text: str):
        posts_text_list = self.find_all(self._POST_ITEM_CONTENT_TEXT)
        for post in posts_text_list:
            if post_text in post.text:
                self.click(self._POST_ITEM_ACTION_DROPDOWN)
                self.click(self._POST_ITEM_DELETE_BUTTON)

    @allure.step("Check Post Deleted")
    def is_post_deleted(self, post_text: str):
        posts_text_list = self.find_all(self._POST_ITEM_CONTENT_TEXT)
        for post in posts_text_list:
            if post_text in post.text:
                raise AssertionError("Post was not deleted")

    @allure.step("Edit a Post")
    def edit_post(self, post_text, edited_post_text):
        posts_text_list = self.find_all(self._POST_ITEM_CONTENT_TEXT)
        for post in posts_text_list:
            if post_text in post.text:
                self.click(self._POST_ITEM_ACTION_DROPDOWN)
                self.click(self._POST_ITEM_EDIT_BUTTON)
                self.wait_visibility_of_element(self._POST_EDIT_SAVE_BUTTON)

                self.find(self._POST_EDIT_TEXT_INPUT).clear()
                self.fill(self._POST_EDIT_TEXT_INPUT, edited_post_text)
                assert edited_post_text == self.find(self._POST_EDIT_TEXT_INPUT).get_attribute("value"), f"The input area does not contain '{edited_post_text}'"

                self.click(self._POST_EDIT_SAVE_BUTTON)
                return True

        raise AssertionError("Required post not found")

    @allure.step("Check Post Edited")
    def is_post_edited(self, edited_post_text):
        self.wait_visibility_of_element(self._SUCCESS_ALERT)
        assert "Post successfully saved" == self.find(self._SUCCESS_ALERT).text, "Something went wrong"

        posts_text_list = self.find_all(self._POST_ITEM_CONTENT_TEXT)
        for post in posts_text_list:
            if edited_post_text in post.text:
                return True
        raise AssertionError("Post was not edited")