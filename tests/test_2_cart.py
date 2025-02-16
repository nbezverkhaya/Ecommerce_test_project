import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser import get_driver
from utils import config
from Pages.base_page import HomePage
from Pages.cart_page import CartPage
@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_and_add_to_cart(driver):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, config.LOG_IN_LINK)))
    home_page.open_login()
    home_page.login(config.USER_NAME_2, config.PASSWORD_2)

    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "nameofuser"), f"Welcome {config.USER_NAME_2}"))
    username_display = driver.find_element(By.ID, "nameofuser").text
    assert f"Welcome {config.USER_NAME_2}" in username_display

    home_page.add_product_to_cart(config.PRODUCT_1)
    driver.get(config.BASE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, config.PRODUCT_2)))
    home_page.add_product_to_cart(config.PRODUCT_2)

    cart_page.open_cart()
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, config.ITEMS_IN_THE_CART)))
    items_in_cart = cart_page.get_cart_items()
    WebDriverWait(driver, 10).until(lambda d: config.PRODUCT_1 in items_in_cart and config.PRODUCT_2 in items_in_cart)
    assert config.PRODUCT_1 in items_in_cart
    assert config.PRODUCT_2 in items_in_cart

# Why were the three tests merged into one?
#
# In a real-world project, it would be best practice to keep these as three separate tests:
#
# Login Test – Verifying that the user can log in successfully.
# Add to Cart Test – Ensuring that items can be added to the cart.
# Cart Validation Test – Checking that the correct items appear in the cart.

# However, on this specific test website, there is an issue with caching that affects session management. When a new test starts, the browser does not always retain the user's login session, causing inconsistencies in the cart contents.
#
# To ensure that the tests run reliably, they were merged into a single test where:
#
# The user logs in.
# Items are added to the cart.
# The cart contents are validated within the same session.
# This guarantees that the logged-in user's session is maintained throughout the test, avoiding unexpected behavior caused by session resets.