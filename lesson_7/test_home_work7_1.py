import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from form_page import FormPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_form(driver):
    form_page = FormPage(driver)

    form_page.open()

    field_names = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "zip-code", "city", "country",
        "job-position", "company"
    ]

    values = [
        "Иван", "Петров", "Ленина, 55-3", "test@skypro.com",
        "+7985899998787", "", "Москва", "Россия",
        "QA", "SkyPro"
    ]

    form_page.fill_form(field_names, values)

    form_page.submit()

    form_page.company_element()

    assert "danger" in form_page.get_zip_code_class(), "Поле Zip code должно быть подсвечено красным"

    fields = [
        "first-name", "last-name", "address", "e-mail",    ]
    for field_id in fields:
        assert "success" in form_page.get_class(field_id), f"Поле {field_id} должно быть подсвечено зеленым"


    print("well done")