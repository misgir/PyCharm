import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self._driver = driver

class FormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    @allure.step('Открываем страницу')
    def open(self):
        self._driver.get(self.url)

    @allure.step('Заполняем форму')
    def fill_form(self, field_names, values):
         for name, value in zip(field_names, values):
            self.wait_for_element(By.NAME, name).send_keys(value)

    @allure.step('Нажимаем на кнопку submit')
    def submit(self):
         self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    @allure.step('Получение элемента')
    def wait_for_element(self, by, value):
         return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((by, value)))

    def company_element(self):
         WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "company"))
        )

    @allure.step("Проверяем что поле zip code подсвечено красным")
    def get_zip_code_class(self):
         return self._driver.find_element(By.ID, "zip-code").get_attribute("class")

    @allure.step("Проверяем что остальные поля зеленые")
    def get_class(self, field_id):
         return self._driver.find_element(By.ID, field_id).get_attribute("class")