from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

name = "body > main > div > form > div:nth-child(1) > div:nth-child(1) > label > input"

first_name = browser.find_element(By.CSS_SELECTOR, name)

first_name.send_keys("Иван")

name2 = "body > main > div > form > div:nth-child(1) > div:nth-child(2) > label > input"

last_name = browser.find_element(By.CSS_SELECTOR, name2).send_keys("Петров")
name3 = "body > main > div > form > div:nth-child(2) > div.col-md-4.py-2 > label > input"

address = browser.find_element(By.CSS_SELECTOR, name3).send_keys("Ленина, 55-3")
name4 = "body > main > div > form > div:nth-child(2) > div.col-md-2.py-2 > label > input"

zip = browser.find_element(By.CSS_SELECTOR, name4).send_keys("")
name5 = "body > main > div > form > div:nth-child(2) > div:nth-child(3) > label > input"

city = browser.find_element(By.CSS_SELECTOR, name5).send_keys("Москва")
name6 = "body > main > div > form > div:nth-child(2) > div:nth-child(4) > label > input"

country = browser.find_element(By.CSS_SELECTOR, name6).send_keys("Россия")
name7 = "body > main > div > form > div:nth-child(3) > div:nth-child(1) > label > input"

email = browser.find_element(By.CSS_SELECTOR, name7).send_keys("test@skypro.com")
name8 = "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input"

phone_num = browser.find_element(By.CSS_SELECTOR, name8).send_keys("+7985899998787")
name9 = "body > main > div > form > div:nth-child(4) > div:nth-child(1) > label > input"

job_position = browser.find_element(By.CSS_SELECTOR, name9).send_keys("QA")
name10 = "body > main > div > form > div:nth-child(4) > div:nth-child(2) > label > input"

company = browser.find_element(By.CSS_SELECTOR, name10).send_keys("SkyPro")

button = "body > main > div > form > div:nth-child(5) > div > button"

submit = browser.find_element(By.CSS_SELECTOR, button).click()