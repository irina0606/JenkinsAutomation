import time
from pages.dashboard_page import DashboardPage

def test_open_dashboardDropdown(logged_in_driver): # it is a defect
    dashboardPage = DashboardPage(logged_in_driver)
    dashboardPage.open_dashboardDropdown()
    element = logged_in_driver.find_element(*dashboardPage.dashboard_dropdown)
    time.sleep(5)
    assert element.is_displayed(), "Dashboard dropdown menu did not open as expected"

#def test_open_systemConfig_frame(logged_in_driver, driver):

def test_new_item_link(logged_in_driver):
    dashboardPage = DashboardPage(logged_in_driver)
    dashboardPage.navigate_to_new_item_page()
    assert logged_in_driver.current_url == "http://localhost:8080/view/all/newJob", \
        "Did not navigate to the New Item page"