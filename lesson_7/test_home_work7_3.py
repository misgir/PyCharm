import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_page import ShopPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@allure.feature('ДЗ 7')
@allure.title('Автотест работы магазина')
@allure.description('Добавление товаров в корзину и проверка итоговой суммы')
@allure.severity(allure.severity_level.CRITICAL)
def test_purchase_total(driver):
    shop_page = ShopPage(driver)

    shop_page.open()

    shop_page.login('standard_user', 'secret_sauce')

    items_to_add = [
        'sauce-labs-backpack',
        'sauce-labs-bolt-t-shirt',
        'sauce-labs-onesie'
    ]
    shop_page.add_to_cart(items_to_add)

    shop_page.cart()
    shop_page.checkout('alina', 'ivanovna', '123444')

    total = shop_page.get_total()
    print(total)

    assert total == 'Total: $58.29', f"''{total}'"

    print("well done!")