import platform
import allure
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


class UIHelper:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1)
        self.actions = ActionChains(self.driver)

    def open(self):
        with allure.step(f"Open Page: '{self._PAGE_URL}'"):
            self.driver.get(self._PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page: '{self._PAGE_URL}' is opened"):
            self.wait.until(EC.url_to_be(self._PAGE_URL))

    def is_opened_user_admin(self, role="user"):
        if role == "user":
            with allure.step(f"Page: '{self._PAGE_URL_USER}' is opened"):
                self.wait.until(EC.url_to_be(self._PAGE_URL_USER))
        else:
            with allure.step(f"Page: '{self._PAGE_URL_ADMIN}' is opened"):
                self.wait.until(EC.url_to_be(self._PAGE_URL_ADMIN))

    @property
    def cmd_ctr_button(self):
        os_name = platform.system()
        cmd_ctrl_button = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL
        return cmd_ctrl_button

    # Elements
    def find(self, locator: tuple) -> WebElement:
        element = self.wait_visibility_of_element(locator)
        return element

    def find_all(self, locator: tuple) -> list[WebElement]:
        elements = self.wait_visibility_of_elements(locator)
        return elements

    def fill(self, locator: tuple, text: str):
        self.find(locator).send_keys(text)

    def click(self, locator: tuple):
        self.wait_element_to_be_clickable(locator).click()

    # Waits
    def wait_visibility_of_element(self, locator: tuple, message=None) -> WebElement:
        element = self.wait.until(EC.visibility_of_element_located(locator), message=message)
        return element

    def wait_visibility_of_elements(self, locator: tuple, message=None) -> list[WebElement]:
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator), message=message)
        return elements

    def wait_invisibility_of_element(self, locator: tuple, message=None) -> WebElement:
        element = self.wait.until(EC.invisibility_of_element_located(locator), message=message)
        return element

    def wait_element_to_be_clickable(self, locator: tuple, message=None) -> WebElement:
        element = self.wait.until(EC.element_to_be_clickable(locator), message=message)
        return element

    def wait_text_to_be_present_in_element_attribute(self, locator: tuple, attribute: str, text: str, message=None) -> bool:
        element = self.wait.until(EC.text_to_be_present_in_element_attribute(locator, attribute, text),  message=message)
        return element

    def wait_url_to_be(self, url: str, message=None) -> bool:
        element = self.wait.until(EC.url_to_be(url), message=message)
        return element

    # Scrolls
    def scroll_by(self, x: int, y: int):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'instant' });")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo({ top: 0, behavior: 'instant' });")

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", element)
