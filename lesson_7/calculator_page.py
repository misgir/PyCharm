import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self._driver = driver

class CalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    @allure.step('Открываем сайт')
    def open(self):
         self._driver.get(self.url)

    @allure.step('В поле ввода по локатору delay вводим значение 45')
    def set_delay(self, delay):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "input#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step('Нажимаем на кнопку')
    def button(self, button_text):
        button = self._driver.find_element(By.XPATH, f'//span[text()="{button_text}"]')
        button.click()

    @allure.step('Получаем результат')
    def result(self):
         return self._driver.find_element(By.CSS_SELECTOR, ".screen").text

    @allure.step('Проверяем что в окне отобразится результат 15 через 45 секунд')
    def wait_for_result(self, expected_result):
         WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected_result)
         )