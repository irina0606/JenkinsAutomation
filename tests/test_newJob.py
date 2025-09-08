from selenium.webdriver.support.wait import WebDriverWait
from utils.waits import *
from pages.newJob_page import NewJob
from selenium.webdriver.support import expected_conditions as EC

def test_create_new_item(logged_in_driver):
    logged_in_driver.get("http://localhost:8080/view/all/newJob")
    item_name = "Ira_004"
    created_item_endpoint = f"/job/{item_name}/configure"
    newJobPage = NewJob(logged_in_driver)
    newJobPage.create_new_item(item_name)
    wait_url_contains(logged_in_driver, created_item_endpoint)
    assert created_item_endpoint in logged_in_driver.current_url