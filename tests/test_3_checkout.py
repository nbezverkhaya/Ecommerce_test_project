import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import get_driver
from utils import config
from Pages.cart_page import CartPage
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(config.CART_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_place_order(driver):
    cart_page = CartPage(driver)
    cart_page.open_cart()
    time.sleep(2)
    cart_page.open_order_modal()
    time.sleep(2)
    cart_page.fill_checkout_form()
    time.sleep(1)
    cart_page.confirm_purchase()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert")))
    alert_text = driver.find_element(By.XPATH, "//div[contains(@class, 'sweet-alert')]//h2").text
    print("Alert Message:", alert_text)
    assert "Thank you for your purchase!" in alert_text, "Purchase confirmation not found!"