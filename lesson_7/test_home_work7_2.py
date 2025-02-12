import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.feature('ДЗ 7')
@allure.title('Автотест с проверкой работы калькулятора')
@allure.description('Ввод цифр и ожидание результата')
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    calculator_page = CalculatorPage(driver)

    calculator_page.open()

    calculator_page.set_delay("45")

    calculator_page.button("7")
    calculator_page.button("+")
    calculator_page.button("8")
    calculator_page.button("=")

    calculator_page.wait_for_result("15")

    result = calculator_page.result()
    assert int(result) == 15, f"результат {result}"

    print("well done")