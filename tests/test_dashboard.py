from pages.dashboard_page import DashboardPage

def test_open_dashboardDropdown(logged_in_driver):
    dashboardPage = DashboardPage(logged_in_driver)
    dashboardPage.open_dashboardDropdown(logged_in_driver)
    element = logged_in_driver.find_element(*dashboardPage.dashboard_dropdown)
    assert element.is_displayed(), "Dashboard dropdown menu did not open as expected"

#def test_open_systemConfigs(logged_in_driver, driver):