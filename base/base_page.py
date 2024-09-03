import allure
from base.base_components.groups_dropdown import GroupsDropdown
from base.base_components.links_dropdown import LinksDropdown
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator


class BasePage(UIHelper, metaclass=MetaLocator):

    _LINKS_DROPDOWN = "//div[@class='sidebar-menu']//a[text()='Links']"
    _GROUPS_DROPDOWN = "//div[@class='sidebar-menu']//a[text()='Groups']"

    def __init__(self, driver):
        super().__init__(driver)
        self.links_dropdown = LinksDropdown(self.driver)
        self.groups_dropdown = GroupsDropdown(self.driver)

    @allure.step("Open | Close Links Dropdown")
    def click_links_dropdown(self):
        self.click(self._LINKS_DROPDOWN)

    @allure.step("Open | Close Links Dropdown")
    def click_groups_dropdown(self):
        self.click(self._GROUPS_DROPDOWN)