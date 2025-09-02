from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from utils.helpers import click_element, hover_element
from utils.waits import wait_until_visible, wait_until_present


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.dashboard_button = (By.XPATH, '//*[@id="breadcrumbs"]/li[1]')
        self.dashboard_chevron = (By.CSS_SELECTOR, ".jenkins-menu-dropdown-chevron")
        self.dashboard_dropdown = (By.CLASS_NAME, "tippy-box")
        self.manageJenkins_chevron = (By.XPATH, "//a[normalize-space()='Manage Jenkins']")
        self.manageJenkins = (By.XPATH, "//a[@class='jenkins-dropdown__item '][normalize-space()='Manage Jenkins']")
        self.system_configs = (By.XPATH, "//iframe[@id = 'nr-ext-rsicon']")

    def open_dashboardDropdown(self, driver):
        wait_until_visible(self.driver, self.dashboard_button)
        hover_element(self.driver, self.dashboard_button)
        hover_element(self.driver, self.dashboard_chevron)
        click_element(self.driver, self.dashboard_chevron)
        wait_until_visible(self.driver, self.dashboard_dropdown)

    def open_systemConfigs(self, driver):
        self.open_dashboardDropdown(driver)
        wait_until_visible(self.driver, self.dashboard_dropdown)
        hover_element(self.driver, self.manageJenkins)
        iframe = driver.find_element(self.system_configs)
        driver.switch_to.frame(iframe)
        wait_until_present(self.driver, self.system_configs)





