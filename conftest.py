import pytest
from selenium import webdriver
from pages.login_page import LoginPage  # adjust import as needed
from dotenv import load_dotenv
import os
from utils.waits import wait_for_title


@pytest.fixture(scope="session")
def driver_factory():
    drivers = []

    def _create_driver():
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080")
        drivers.append(driver)
        return driver

    yield _create_driver

    for driver in drivers:
        driver.quit()

@pytest.fixture(scope="session")
def credentials():
    username = os.getenv("LOGIN_USERNAME")
    password = os.getenv("LOGIN_PASSWORD")
    return username, password

@pytest.fixture(scope="function")
def logged_in_driver(driver_factory, credentials):
    driver = driver_factory()
    username, password = credentials
    login_page = LoginPage(driver)
    login_page.login(username, password)
    driver.find_element(*login_page.login_button).click()  # 🔥 perform the click
    wait_for_title(driver, "Dashboard [Jenkins]")
    yield driver
    driver.quit()

load_dotenv()


