from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://www.saucedemo.com/")

input_username = "#user-name"
input_password = "#password"

search_input = browser.find_element(By.CSS_SELECTOR, input_username)
search_input.send_keys("standard_user")

search_input = browser.find_element(By.CSS_SELECTOR, input_password)
search_input.send_keys("secret_sauce")

button = "#login-button"
search_button = browser.find_element(By.CSS_SELECTOR, button).click()

add_to_cart1 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

 add_to_cart2 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

 add_to_cart3 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

 cart = browser.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a").click()


checkout = browser.find_element(By.CSS_SELECTOR, "#checkout").click()


name = browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys("alina")

last_name = browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys("ivanovna")

code = browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(111222)


button_continue = browser.find_element(By.CSS_SELECTOR, "#continue").click()


total = browser.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label")

print(total.text)

quit()
