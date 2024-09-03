import os
import sys
import pytest
from selenium import webdriver


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(autouse=True)
def driver(request):
    driver = get_driver()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def add_users(request):
    user_count = request.param  # Принимаем кол-во юзеров из параметров теста
    drivers = []
    for _ in range(user_count):
        driver = get_driver()
        drivers.append(driver)
    yield drivers
    for driver in drivers:
        driver.quit()


@pytest.fixture(autouse=True, scope="session")
def setup_allure_environment_properties():
    properties = {
        # "Stage": os.environ["STAGE"],
        # "Browser": os.environ["BROWSER"],
        "Python Version": f"{sys.version}"
    }
    with open("allure-results/environment.properties", "w") as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")