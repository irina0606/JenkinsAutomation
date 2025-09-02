import pytest
from selenium import webdriver
from pages.login_page import LoginPage  # adjust import as needed
from dotenv import load_dotenv
import os

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def logged_in_driver(driver):
    username = os.getenv("LOGIN_USERNAME")
    password = os.getenv("LOGIN_PASSWORD")

    login_page = LoginPage(driver)
    login_page.login(username, password)
    return driver

@pytest.fixture(scope="session")
def credentials():
    username = os.getenv("LOGIN_USERNAME")
    password = os.getenv("LOGIN_PASSWORD")
    return username, password

load_dotenv()


