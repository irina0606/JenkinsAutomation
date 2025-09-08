import time

from selenium.webdriver.common.by import By
from utils.helpers import click_element
from utils.waits import *


class NewJob:
    def __init__(self, driver):
        self.driver = driver
        self.item_name_field = (By.CSS_SELECTOR, "#name")
        self.freestyle_project_icon = (By.XPATH, "//label[contains(., 'Freestyle project')]")
        self.ok_button = (By.ID, "ok-button")

    def create_new_item(self, item_name):
        self.driver.find_element(*self.item_name_field).send_keys(item_name)
        wait_until_clickable(self.driver, self.freestyle_project_icon).click()
        click_element(self.driver, self.ok_button)

