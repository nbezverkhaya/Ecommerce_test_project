import time
import pytest
from selenium.webdriver.common.by import By
from browser import get_driver
import config

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()  # Використовуємо функцію get_driver()
    driver.get(config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_positive_registration(driver):
    driver.find_element(By.ID, config.SIGN_IN_BUTTON).click()
    time.sleep(2)

    driver.find_element(By.ID, config.USER_NAME_FIELD).send_keys(config.VALID_USERNAME)
    driver.find_element(By.ID, config.PASSWORD_FIELD).send_keys(config.VALID_PASSWORD)
    driver.find_element(By.XPATH, config.SIGN_UP_BUTTON).click()
    time.sleep(2)

    alert = driver.switch_to.alert
    assert "Sign up successful" in alert.text
    alert.accept()

def test_negative_registration(driver):
    driver.find_element(By.ID, config.SIGN_IN_BUTTON).click()
    time.sleep(2)

    driver.find_element(By.ID, config.USER_NAME_FIELD).send_keys(config.VALID_USERNAME)
    driver.find_element(By.ID, config.PASSWORD_FIELD).send_keys(config.VALID_PASSWORD)
    driver.find_element(By.XPATH, config.SIGN_UP_BUTTON).click()
    time.sleep(2)

    alert = driver.switch_to.alert
    assert "This user already exist." in alert.text
    alert.accept()

def test_positive_login(driver):
    driver.find_element(By.XPATH, config.LOG_IN_LINK).click()
    time.sleep(2)

    driver.find_element(By.ID, config.LOG_IN_USER_NAME_FIELD).send_keys(config.VALID_USERNAME)
    driver.find_element(By.ID, config.LOG_IN_PASSWORD_FIELD).send_keys(config.VALID_PASSWORD)
    driver.find_element(By.XPATH, config.LOG_IN_BUTTON).click()
    time.sleep(3)

    assert driver.find_element(By.ID, "nameofuser").text == f"Welcome {config.VALID_USERNAME}"

def test_negative_login(driver):
    driver.find_element(By.XPATH, config.LOG_IN_LINK).click()
    time.sleep(2)

    driver.find_element(By.ID, config.LOG_IN_USER_NAME_FIELD).send_keys(config.INVALID_USERNAME)
    driver.find_element(By.ID, config.LOG_IN_PASSWORD_FIELD).send_keys(config.INVALID_PASSWORD)
    driver.find_element(By.XPATH, config.LOG_IN_BUTTON).click()
    time.sleep(2)

    alert = driver.switch_to.alert
    assert "Wrong password." in alert.text or "User does not exist." in alert.text
    alert.accept()