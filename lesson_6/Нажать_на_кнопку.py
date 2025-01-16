from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))

driver.maximize_window()

driver.get("http://uitestingplayground.com/ajax")

driver.implicitly_wait(30)

# blue_button_id = "#ajaxButton"
button = (driver.find_element(By.CSS_SELECTOR, "#ajaxButton"))
button.click()

element = (driver.find_element(By.CSS_SELECTOR, ".bg-success"))

print(element.text)

driver.quit()
