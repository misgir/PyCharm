from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

add_element_button_locator = "button.btn.btn-primary"
blue_button = driver.find_element(By.CSS_SELECTOR,add_element_button_locator)
blue_button.click()

