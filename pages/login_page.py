from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_field = (By.ID, "j_username")
        self.password_field = (By.ID, "j_password")
        self.login_button = (By.XPATH, "//button[contains(text(), 'Sign in')]")
        self.error = (By.XPATH, "//*[contains(text(), 'Invalid username or password')]")
        self.remember_me_checkbox = (By.ID, "remember_me")
        self.logged_in_indicator = (By.ID, "visible-am-button")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()



