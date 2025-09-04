from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver_factory
from utils.helpers import click_element, hover_element
from utils.waits import wait_until_visible, wait_until_present


class DashboardPage:

    def __init__(self, driver_factory):
        self.driver = driver_factory
        self.dashboard_button = (By.XPATH, '//*[@id="breadcrumbs"]/li[1]')
        self.dashboard_chevron = (By.CSS_SELECTOR, ".jenkins-menu-dropdown-chevron")
        self.dashboard_dropdown = (By.CLASS_NAME, "tippy-box")
        self.manageJenkins_chevron = (By.XPATH, "//a[normalize-space()='Manage Jenkins']")
        self.manageJenkins = (By.XPATH, "//a[@class='jenkins-dropdown__item '][normalize-space()='Manage Jenkins']")
        self.system_configs = (By.XPATH, "//iframe[@id = 'nr-ext-rsicon']")

    def open_dashboardDropdown(self, driver_factory):
        wait_until_visible(self.driver, self.dashboard_button)
        hover_element(self.driver, self.dashboard_button)
        hover_element(self.driver, self.dashboard_chevron)
        click_element(self.driver, self.dashboard_chevron)
        wait_until_visible(self.driver, self.dashboard_dropdown)

    def open_systemConfigs(self, driver_factory):
        self.open_dashboardDropdown(driver_factory)
        wait_until_visible(self.driver, self.dashboard_dropdown)
        hover_element(self.driver, self.manageJenkins)
        iframe = driver_factory.find_element(self.system_configs)
        driver_factory.switch_to.frame(iframe)
        wait_until_present(self.driver, self.system_configs)





