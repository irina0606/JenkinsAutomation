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
        self.dashboard_element = (By.XPATH, '//*[@id="breadcrumbs"]/li[1]')
        self.dashboard_chevron = (By.CSS_SELECTOR, ".jenkins-menu-dropdown-chevron")
        self.dashboard_dropdown = (By.XPATH, "//div[@data-placement='bottom-start']")
        self.manageJenkins_chevron = (By.XPATH, "//a[normalize-space()='Manage Jenkins']")
        self.manageJenkins = (By.XPATH, "//a[@class='jenkins-dropdown__item '][normalize-space()='Manage Jenkins']")
        self.system_configs = (By.XPATH, "//iframe[@id = 'nr-ext-rsicon']")
        self.new_item = (By.CLASS_NAME, "task-link-wrapper")

    def open_dashboardDropdown(self):
        wait_until_visible(self.driver, self.dashboard_element)
        hover_element(self.driver, self.dashboard_element)
        hover_element(self.driver, self.dashboard_chevron)
        click_element(self.driver, self.dashboard_chevron)
        wait_until_visible(self.driver, self.dashboard_dropdown)

    def open_systemConfig_frame(self):
        self.open_dashboardDropdown()
        wait_until_visible(self.driver, self.dashboard_dropdown)
        hover_element(self.driver, self.manageJenkins)
        iframe = self.driver.find_element(self.system_configs)
        self.driver.switch_to.frame(iframe)
        wait_until_present(self.driver, self.system_configs)

    def navigate_to_new_item_page(self):
        wait_until_visible(self.driver, self.new_item)
        hover_element(self.driver, self.new_item)
        click_element(self.driver, self.new_item)




