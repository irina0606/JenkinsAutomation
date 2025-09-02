from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.waits import wait_until_clickable
from selenium.webdriver import ActionChains


def open_url(driver, url):
    driver.get(url)

def get_title(driver):
    return driver.title

def get_error_message(driver, error):
    error_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(error)
    )
    return error_element.text

def get_text(driver):
    return driver.text

def get_iframe(driver, iframe):
    driver.switch_to.frame(iframe)

def click_element(driver, locator, timeout=5):
    wait_until_clickable(driver, locator, timeout).click()

def hover_element(driver, locator):
    element = driver.find_element(*locator)
    ActionChains(driver).move_to_element(element).perform()

def tick_checkbox(checkbox_element):
    if not checkbox_element.is_selected():
        checkbox_element.click()

