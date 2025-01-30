from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def find_element_by(browser: Chrome, by: By, path: str) -> WebElement:
    return browser.find_element(by, path)


def test_fields_color() -> None:
    browser = Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name_id = "first-name"
    last_name_id = "last-name"
    address_id = "address"
    zip_id = "zip-code"
    city_id = "city"
    country_id = "country"
    email_id = "e-mail"
    phone_id = "phone"
    job_id = "job-position"
    company_id = "company"

    find_element_by(browser, By.NAME, first_name_id).send_keys("Иван")
    find_element_by(browser, By.NAME, last_name_id).send_keys("Петров")
    find_element_by(browser, By.NAME, address_id).send_keys("Ленина, 55-3")
    find_element_by(browser, By.NAME, zip_id).send_keys("")
    find_element_by(browser, By.NAME, city_id).send_keys("Москва")
    find_element_by(browser, By.NAME, country_id).send_keys("Россия")
    find_element_by(browser, By.NAME, email_id).send_keys("test@skypro.com")
    find_element_by(browser, By.NAME, phone_id).send_keys("+7985899998787")
    find_element_by(browser, By.NAME, job_id).send_keys("QA")
    find_element_by(browser, By.NAME, company_id).send_keys("SkyPro")

    button_path = "body > main > div > form > div:nth-child(5) > div > button"
    button = browser.find_element(By.CSS_SELECTOR, button_path)
    ActionChains(browser).move_to_element(button).perform()
    button.click()

    first_name = find_element_by(browser, By.ID, first_name_id)
    last_name = find_element_by(browser, By.ID, last_name_id)
    address = find_element_by(browser, By.ID, address_id)
    zip_code = find_element_by(browser, By.ID, zip_id)
    city = find_element_by(browser, By.ID, city_id)
    country = find_element_by(browser, By.ID, country_id)
    email = find_element_by(browser, By.ID, email_id)
    phone = find_element_by(browser, By.ID, phone_id)
    job = find_element_by(browser, By.ID, job_id)
    company = find_element_by(browser, By.ID, company_id)

    green_color = "#0f5132"
    red_color = "#842029"

    assert Color.from_string(zip_code.value_of_css_property("color")).hex == red_color
    assert (
        Color.from_string(first_name.value_of_css_property("color")).hex
        == Color.from_string(first_name.value_of_css_property("color")).hex
        == Color.from_string(last_name.value_of_css_property("color")).hex
        == Color.from_string(address.value_of_css_property("color")).hex
        == Color.from_string(city.value_of_css_property("color")).hex
        == Color.from_string(country.value_of_css_property("color")).hex
        == Color.from_string(email.value_of_css_property("color")).hex
        == Color.from_string(phone.value_of_css_property("color")).hex
        == Color.from_string(job.value_of_css_property("color")).hex
        == Color.from_string(company.value_of_css_property("color")).hex
        == green_color
    )


if __name__ == "__main__":
    test_fields_color()
