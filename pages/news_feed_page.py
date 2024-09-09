import allure
from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.links import Links


class NewsFeedPage(BasePage):

    _PAGE_URL = Links.NEWS_FEED_PAGE

    _POST_TEXT_INPUT = "//textarea[@name='post']"
    _POST_BUTTON = "//input[@type='submit']"

    _POSTS_ITEMS_LIST = "//div[@class='user-activity']/div[descendant::a[@data-bs-toggle='dropdown']]"
    _POST_ITEM_CONTENT_TEXT = ".//div[@class='post-contents']"
    _POST_ITEM_ACTION_DROPDOWN = ".//a[@data-bs-toggle='dropdown']"
    _POST_ITEM_EDIT_BUTTON = ".//a[text()='Edit']"
    _POST_ITEM_DELETE_BUTTON = ".//a[text()='Delete']"

    _POST_EDIT_SAVE_BUTTON = "//div[@class='control']//a[text()='Save']"
    _POST_EDIT_TEXT_INPUT = "//textarea[@id='post-edit']"

    @property
    def _posts_items_list(self):
        return self.find_all(self._POSTS_ITEMS_LIST)

    # Posts
    @allure.step("Enter Post Text")
    def enter_post_text(self, post_text: str):
        self.wait_element_to_be_clickable(self._POST_TEXT_INPUT)
        self.find(self._POST_TEXT_INPUT).clear()
        self.fill(self._POST_TEXT_INPUT, post_text)
        assert post_text == self.find(self._POST_TEXT_INPUT).get_attribute("value"), f"The input area does not contain '{post_text}'"

    @allure.step("Click 'Post' Button")
    def click_post_button(self):
        self.click(self._POST_BUTTON)
        self.wait_element_to_be_clickable(self._POST_BUTTON)

    def get_post_id(self, post_text: str = None):
        if post_text:
            for post_item in self._posts_items_list:
                item = post_item.find_element(*self._POST_ITEM_CONTENT_TEXT)
                if post_text == item.text:
                    return post_item.get_attribute("id")
        else:
            posts_items_list = self._posts_items_list
            return posts_items_list[0].get_attribute("id")

    @allure.step("Check Post Created")
    def is_post_created(self, post_id: str):
        posts_items_list = self._posts_items_list
        assert posts_items_list[0].get_attribute("id") == post_id, f"Post with id '{post_id}' was not created."

    @allure.step("Edit a Post")
    def edit_post(self, new_post_text: str, post_id: str = None, post_text: str = None) -> WebElement:
        if not post_id and not post_text:
            raise ValueError("Either 'post_id' or 'post_text' must be provided.")

        post_item = self._find_post_item(post_text=post_text, post_id=post_id)
        if post_item is None:
            raise AssertionError("Required post not found.")

        self._edit_post_item(post_item, new_post_text)
        return post_item

    def _find_post_item(self, post_text: str = None, post_id: str = None):
        for post_item in self._posts_items_list:
            if post_id and post_id == post_item.get_attribute("id"):
                return post_item
            elif post_text and post_text == post_item.find_element(*self._POST_ITEM_CONTENT_TEXT).text:
                return post_item
        return None

    def _edit_post_item(self, post_item, new_post_text: str):
        self.scroll_to_element(post_item)
        action_button = post_item.find_element(*self._POST_ITEM_ACTION_DROPDOWN)
        action_button.click()
        edit_button = post_item.find_element(*self._POST_ITEM_EDIT_BUTTON)
        edit_button.click()

        self.find(self._POST_EDIT_TEXT_INPUT).clear()
        self.fill(self._POST_EDIT_TEXT_INPUT, new_post_text)
        assert new_post_text == self.find(self._POST_EDIT_TEXT_INPUT).get_attribute("value"), f"The input area does not contain '{new_post_text}'."

        self.click(self._POST_EDIT_SAVE_BUTTON)

    @allure.step("Check Post Edited")
    def is_post_edited(self, new_post_text: str, post_id: str):
        self.wait_visibility_of_element(self._SUCCESS_ALERT)
        assert "Post successfully saved" == self.find(self._SUCCESS_ALERT).text, "Something went wrong."

        post_item = self._find_post_item(post_id=post_id)
        if post_item is None:
            raise AssertionError("Required post was not found.")

        actual_text = post_item.find_element(*self._POST_ITEM_CONTENT_TEXT).text
        assert new_post_text == actual_text, "Post was not edited."

    @allure.step("Delete a Post")
    def delete_post(self, post_text: str = None, post_id: str = None) -> WebElement:
        if not post_text and not post_id:
            raise ValueError("Either 'post_text' or 'post_id' must be provided.")

        posts_items_list = self._posts_items_list
        for post_item in posts_items_list:
            if post_id:
                item_id = post_item.get_attribute("id")
                if post_id == item_id:
                    self._delete_post_item(post_item)
                    return post_item
            elif post_text:
                item_text = post_item.find_element(*self._POST_ITEM_CONTENT_TEXT).text
                if post_text == item_text:
                    self._delete_post_item(post_item)
                    return post_item

        raise AssertionError(f"Post with text '{post_text}' or ID '{post_id}' does not exist.")

    def _delete_post_item(self, post_item):
        action_button = post_item.find_element(*self._POST_ITEM_ACTION_DROPDOWN)
        action_button.click()
        delete_button = post_item.find_element(*self._POST_ITEM_DELETE_BUTTON)
        delete_button.click()

    @allure.step("Check Post Deleted")
    def is_post_deleted(self, post_id: str) -> bool:
        posts_items_list = self._posts_items_list
        if posts_items_list is None:
            return True

        for post_item in posts_items_list:
            item_id = post_item.get_attribute("id")

            if post_id == item_id:
                raise AssertionError(f"Post with ID '{post_id}' was not deleted.")

        return True
