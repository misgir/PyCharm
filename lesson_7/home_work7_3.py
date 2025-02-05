import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from shop_page import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_shop(driver):
    shop_page = ShopPage(driver)

    shop_page.open()

    shop_page.login('standard_user', 'secret_sauce')

    items_to_add = [
        'sauce-labs-backpack',
        'sauce-labs-bolt-t-shirt',
        'sauce-labs-onesie'
    ]
    shop_page.add_cart(items_to_add)

    shop_page.go_to_cart()
    shop_page.checkout('alina', 'ivanovna', '111222')

    total = shop_page.get_total()
    print(total)

    assert total == 'Total: $58.29', f"'{total}'"

    print("well done")