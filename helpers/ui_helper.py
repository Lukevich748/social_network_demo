import platform
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
        self.driver.get(self._PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))

    @property
    def cmd_ctr_button(self):
        os_name = platform.system()
        cmd_ctrl_button = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL
        return cmd_ctrl_button

    # Elements
    def find(self, locator: tuple) -> WebElement:
        element = self.wait_visibility_of_element(locator)
        return element

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

    # Scrolls
    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, locator):
        self.actions.scroll_to_element(self.find(locator))
        self.driver.execute_script("""
            window.scrollTo({
                top: window.scrollY + 500,
            });
            """)
