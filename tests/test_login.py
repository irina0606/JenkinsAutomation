from conftest import wait_for_title, login
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_login(driver):

    login_page = LoginPage(driver)

    assert "Sign in [Jenkins]" in driver.title

    login(driver, "admin", "61967968c3b74e92bf820032c5a32df7")
    wait_for_title(driver, "Dashboard")

    assert "Dashboard [Jenkins]" in driver.title


