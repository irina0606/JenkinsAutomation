from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Locate the checkbox
checkbox = driver.find_element(By.ID, "subscribe")

# Check if it's already selected
if not checkbox.is_selected():
    checkbox.click()  # Check the box