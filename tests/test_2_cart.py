
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import get_driver

import config

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_cart():
    driver = get_driver()
    driver.get(config.CART_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_and_add_to_cart(driver):
    # first_test
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, config.LOG_IN_LINK)))
    login_button = driver.find_element(By.XPATH, config.LOG_IN_LINK)
    login_button.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, config.LOG_IN_USER_NAME_FIELD)))
    email_field = driver.find_element(By.ID, config.LOG_IN_USER_NAME_FIELD)
    email_field.send_keys(config.USER_NAME_2)
    password_field = driver.find_element(By.ID, config.LOG_IN_PASSWORD_FIELD)
    password_field.send_keys(config.PASSWORD_2)
    login_submit_button = driver.find_element(By.XPATH, config.LOG_IN_BUTTON)
    login_submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome"))
    username_display = driver.find_element(By.ID, "nameofuser").text
    assert f"Welcome {config.USER_NAME_2}" in username_display, f"Expected username text not found: {username_display}"

    # second_test
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, config.PRODUCT_1)))
    element_1 = driver.find_element(By.LINK_TEXT, config.PRODUCT_1)
    element_1.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, config.ADD_TO_CART_BUTTON)))
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, config.ADD_TO_CART_BUTTON)
    add_to_cart_button.click()
    WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()

    driver.get(config.BASE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, config.PRODUCT_2)))
    element_2 = driver.find_element(By.LINK_TEXT, config.PRODUCT_2)
    element_2.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, config.ADD_TO_CART_BUTTON)))
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, config.ADD_TO_CART_BUTTON)
    add_to_cart_button.click()
    WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()

    # third_test
    driver.get(config.CART_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, config.ITEMS_IN_THE_CART)))
    items = driver.find_elements(By.CSS_SELECTOR, config.ITEMS_IN_THE_CART)

    item_names = [item.find_element(By.XPATH, config.ITEM_NAMES).text for item in items]
    print(f"Items in cart: {item_names}")
    assert config.PRODUCT_1 in item_names, f"{config.PRODUCT_1} is missing from cart"
    assert config.PRODUCT_2 in item_names, f"{config.PRODUCT_2} is missing from cart"

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