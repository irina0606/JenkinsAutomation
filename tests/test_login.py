import json
import time

from selenium.webdriver.chrome import webdriver

from pages import login_page
from utils.waits import *
from utils.helpers import *
from pages.login_page import *
from pages.dashboard_page import *
import pytest

def test_login(driver, credentials):
    username, password = credentials
    login_page = LoginPage(driver)
    print("Actual title:", driver.title)
    assert "Sign in [Jenkins]" in driver.title
    login_page.login(username, password)
    wait_for_title(driver, "Dashboard [Jenkins]")
    assert "Dashboard [Jenkins]" in driver.title


"""def test_login_with_invalid_credentials(driver):
    login_page = LoginPage(driver)

    login_page.login("aaa", "wrongpassword")
    driver.find_element(*login_page.login_button).click()
    error = get_error_message(driver, login_page.error)
    assert "Invalid username or password" in error

def test_login_with_empty_username(driver):
    login_page = LoginPage(driver)

    login_page.login("", "wrongpassword")
    driver.find_element(*login_page.login_button).click()
    error = get_error_message(driver, login_page.error)
    assert "Invalid username or password" in error

def test_login_with_empty_pw(driver):
    login_page = LoginPage(driver)

    login_page.login("aaa", "")
    driver.find_element(*login_page.login_button).click()
    error = get_error_message(driver, login_page.error)
    assert "Invalid username or password" in error"""

@pytest.mark.parametrize("username, pw", [
    ("aaa", "wrongpassword"),
    ("", "wrongpassword"),
    ("aaa", ""),
])

def test_login_invalid_inputs(driver, username, pw):
    login_page = LoginPage(driver)
    login_page.login(username, pw)
    driver.find_element(*login_page.login_button).click()
    error = get_error_message(driver, login_page.error)
    wait_until_visible(driver, login_page.error)
    assert "Invalid username or password" in error


def test_keep_me_signedin(driver, credentials, tmp_path):
    username, pw = credentials
    login_page = LoginPage(driver)
    checkbox = driver.find_element(*login_page.remember_me_checkbox)
    #tick_checkbox(checkbox)
    login_page.login(username, pw)
    tick_checkbox(checkbox)

    """cookies_file = tmp_path / "cookies.json"
    with open(cookies_file, "w") as f:
        json.dump(driver.get_cookies(), f)

    driver.quit()

    new_driver = webdriver.Chrome()
    new_driver.get("http://localhost:8080")

    with open(cookies_file, "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        if 'sameSite' in cookie and cookie['sameSite'] is None:
            cookie.pop('sameSite')
        try:
            new_driver.add_cookie(cookie)
        except Exception as e:
            print(f"Could not add cookie {cookie['name']}: {e}")

    new_driver.refresh()
    login_page_new = LoginPage(new_driver)
    print(login_page_new.logged_in_indicator, type(login_page_new.logged_in_indicator))
    logged_in_element = WebDriverWait(new_driver, 10).until(
        EC.presence_of_element_located(login_page_new.logged_in_indicator)
    )
    assert logged_in_element.is_displayed(), "User is NOT logged in after reopening browser"

    new_driver.quit()
"""