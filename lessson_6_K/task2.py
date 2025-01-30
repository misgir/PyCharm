from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

num1 = browser.find_element(By.CSS_SELECTOR, "#delay")
num1.clear()
num1.send_keys(45)

num2 = browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
num3 = browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()
num4 = browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()
num5 = browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()


quit()
