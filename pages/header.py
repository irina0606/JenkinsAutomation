from selenium.webdriver.common.by import By
from conftest import driver_factory
from utils.helpers import click_element, hover_element
from utils.waits import (wait_until_visible, wait_until_clickable, wait_until_present)
from selenium.common.exceptions import TimeoutException

class Header:
    def __init__(self, driver):
        self.driver = driver
        self.search_icon = (By.ID, "button-open-command-palette")
        self.search_field = (By.ID, "command-bar")
        self.admin_icon = (By.CLASS_NAME, "icon-md")
        self.notification_icon = (By.ID, "visible-am-insertion")
        self.warning_icon = (By.ID, "visible-sec-am-container")
        self.admin_dropdown_button = (By.CLASS_NAME, "jenkins-menu-dropdown-chevron")
        self.admin_dropdown = (By.CLASS_NAME, "jenkins-dropdown")
        self.logout_button = (By.XPATH, "//a[@href='/logout']//*[name()='svg']")
        #self.results = (By.ID, "search-results")
        self.results = (By.CSS_SELECTOR, ".jenkins-command-palette__results__item")
        self.no_result = (By.XPATH, "//*[contains(text(), 'No results for')]")

    def logout(self):
        wait_until_clickable(self.driver, self.logout_button).click()

    """def search(self, text):
        wait_until_clickable(self.driver, self.search_icon).click()
        input_box = self.driver.find_element(*self.search_field)  # Adjust selector
        input_box.clear()
        input_box.send_keys(text)
        #wait_until_visible(self.driver, self.results)
        time.sleep(2)"""

    def search(self, text):
        wait_until_clickable(self.driver, self.search_icon).click()

        input_box = wait_until_visible(self.driver, self.search_field)
        input_box.clear()
        input_box.send_keys(text)

        # Wait for either search results or "no results" message
        try:
            wait_until_visible(self.driver, self.results, timeout=5)
        except TimeoutException:
            wait_until_present(self.driver, self.no_result, timeout=5)

    """def get_results(self):
        return self.driver.find_element(*self.results).text"""

    @property
    def get_results(self):
        elements = self.driver.find_elements(*self.results)  # Adjust if needed
        return [el.text for el in elements if el.text.strip()]

    def get_no_result(self):
        return self.driver.find_element(*self.no_result).text

    def open_adminDropdown(self, driver_factory):
        wait_until_visible(self.driver, self.admin_icon)
        hover_element(self.driver, self.admin_dropdown_button)
        click_element(self.driver, self.admin_dropdown_button)
        wait_until_visible(self.driver, self.admin_dropdown)

