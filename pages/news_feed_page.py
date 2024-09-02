import allure
from base.base_page import BasePage
from data.links import Links


class NewsFeedPage(BasePage):

    _PAGE_URL = Links.HOME_PAGE

    _TEXT_INPUT = "//textarea[@name='post']"
    _POST_BUTTON = "//input[@type='submit']"
    POSTS_LIST = "//div[@class='user-activity']//div[@class='post-contents']"

    @allure.step("Create New Post")
    def create_new_post(self, text: str):
        self.wait_element_to_be_clickable(self._TEXT_INPUT)
        self.find(self._TEXT_INPUT).clear()
        self.fill(self._TEXT_INPUT, text)
        self.click(self._POST_BUTTON)
        self.is_post_created(text)

    def is_post_created(self, text: str):
        posts_list = self.wait_visibility_of_elements(self.POSTS_LIST)
        for post in posts_list:
            print(post.text)