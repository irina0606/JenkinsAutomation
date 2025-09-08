from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_title(driver, title_substring, timeout=5):
    WebDriverWait(driver, timeout).until(
        EC.title_contains(title_substring)
    )

def wait_until_clickable(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def wait_until_visible(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_until_present(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

def wait_until_invisible(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(locator)
    )

def wait_url_contains(driver, endpoint, timeout=5):
    WebDriverWait(driver, timeout).until(
        EC.url_contains(endpoint)
    )

