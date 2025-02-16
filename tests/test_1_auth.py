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

@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(config.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_positive_registration(driver):
    home_page = HomePage(driver)

    home_page.open_sign_up()
    home_page.sign_up(config.VALID_USERNAME, config.VALID_PASSWORD)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    assert "Sign up successful" in alert.text
    alert.accept()

def test_negative_registration(driver):
    home_page = HomePage(driver)

    home_page.open_sign_up()
    home_page.sign_up(config.VALID_USERNAME, config.VALID_PASSWORD)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    assert "This user already exist." in alert.text
    alert.accept()

def test_positive_login(driver):
    home_page = HomePage(driver)
    home_page.open_login()
    home_page.login(config.VALID_USERNAME, config.VALID_PASSWORD)

    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "nameofuser"), f"Welcome {config.VALID_USERNAME}"))
    assert driver.find_element(By.ID, "nameofuser").text == f"Welcome {config.VALID_USERNAME}"

def test_negative_login(driver):
    home_page = HomePage(driver)

    home_page.open_login()
    home_page.login(config.INVALID_USERNAME, config.INVALID_PASSWORD)

    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    assert "Wrong password." in alert.text or "User does not exist." in alert.text
    alert.accept()
