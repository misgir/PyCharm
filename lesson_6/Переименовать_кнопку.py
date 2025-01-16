from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))

driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

# pole_id = "newButtonName"
pole = (driver.find_element(By.CSS_SELECTOR, "#newButtonName"))
pole.send_keys("SkyPro")
# button1_id = "#updatingButton"
button1 = (driver.find_element(By.CSS_SELECTOR, "#updatingButton"))
button1.click()

print(button1.text)
