from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def find_element_by(browser: Chrome, by: By, path: str) -> WebElement:
    return browser.find_element(by, path)

def test_sum_success():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    num1 = browser.find_element(By.CSS_SELECTOR, "#delay")
    num1.clear()
    num1.send_keys(45)

    num2 = browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)")
    ActionChains(browser).move_to_element(num2).perform()
    num2.click()
    num3 = browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)")
    ActionChains(browser).move_to_element(num3).perform()
    num3.click()
    num4 = browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)")
    ActionChains(browser).move_to_element(num4).perform()
    num4.click()
    num5 = browser.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning")
    ActionChains(browser).move_to_element(num5).perform()
    num5.click()

    text = "#calculator > div.top > div"

    sum = browser.find_element(By.CSS_SELECTOR, text)

    print(sum.text)

    assert sum.text == "15"
