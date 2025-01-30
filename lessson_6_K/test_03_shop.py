from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def find_element_by(browser: Chrome, by: By, path: str) -> WebElement:
    return browser.find_element(by, path)

def test_total_sum():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    browser.get("https://www.saucedemo.com/")

    input_username = "#user-name"
    input_password = "#password"

    search_input = browser.find_element(By.CSS_SELECTOR, input_username)
    search_input.send_keys("standard_user")

    search_input = browser.find_element(By.CSS_SELECTOR, input_password)

    search_input.send_keys("secret_sauce")

    button = "#login-button"
    search_button = browser.find_element(By.CSS_SELECTOR, button)
    ActionChains(browser).move_to_element(search_button).perform()
    search_button.click()

    add_to_cart1 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    ActionChains(browser).move_to_element(add_to_cart1).perform()
    add_to_cart1.click()

    add_to_cart2 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    ActionChains(browser).move_to_element(add_to_cart2).perform()
    add_to_cart2.click()

    add_to_cart3 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    ActionChains(browser).move_to_element(add_to_cart3).perform()
    add_to_cart3.click()

    cart = browser.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a")
    ActionChains(browser).move_to_element(cart).perform()
    cart.click()

    checkout = browser.find_element(By.CSS_SELECTOR, "#checkout")
    ActionChains(browser).move_to_element(checkout).perform()
    checkout.click()

    name = browser.find_element(By.CSS_SELECTOR, "#first-name")
    name.send_keys("alina")

    last_name = browser.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("ivanovna")

    code = browser.find_element(By.CSS_SELECTOR, "#postal-code")
    code.send_keys(111222)

    button_continue = browser.find_element(By.CSS_SELECTOR, "#continue")
    ActionChains(browser).move_to_element(button_continue).perform()
    button_continue.click()

    total = browser.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label")

    print(total.text)

    assert total.text ==  "Total: $58.29"