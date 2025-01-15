from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_element_button_locator = "button"
for _ in range(5):
    add_element_button = driver.find_element(By.CSS_SELECTOR, add_element_button_locator)
    add_element_button.click()


add_element_button_locator = "delete"
delete_buttons_locator = "button.added-manually"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, delete_buttons_locator)
print("напечатай чонить:", len(delete_buttons))

