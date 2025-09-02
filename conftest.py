import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def get_title(self):
    return self.driver.title

def wait_for_title(driver, title_substring, timeout=10):
    """Waits until the page title contains the given substring."""
    WebDriverWait(driver, timeout).until(
        EC.title_contains(title_substring)
    )