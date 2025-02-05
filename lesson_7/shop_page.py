from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver

class ShopPage(BasePage):
    def open(self):
        self._driver.get('https://www.saucedemo.com/')
        self._driver.maximize_window()

    def login(self, username, password):
        user_name_input = self._driver.find_element(By.CSS_SELECTOR, '#user-name')
        user_name_input.clear()
        user_name_input.send_keys(username)

        password_input = self._driver.find_element(By.CSS_SELECTOR, '#password')
        password_input.clear()
        password_input.send_keys(password)

        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_cart(self, item_ids):
        for item_id in item_ids:
            self._driver.find_element(By.CSS_SELECTOR, f'#add-to-cart-{item_id}').click()

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    def checkout(self, first_name, last_name, postal_code):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)

        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def get_total(self):
        return self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_lab')
