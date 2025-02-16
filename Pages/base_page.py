from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils.config

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.product_1 = (By.LINK_TEXT, utils.config.PRODUCT_1)
        self.product_2 = (By.LINK_TEXT, utils.config.PRODUCT_2)

    def open_sign_up(self):
        self.driver.find_element(By.ID, utils.config.SIGN_IN_LINK).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, utils.config.USER_NAME_FIELD)))

    def sign_up(self, username, password):
        self.driver.find_element(By.ID, utils.config.USER_NAME_FIELD).send_keys(username)
        self.driver.find_element(By.ID, utils.config.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(By.XPATH, utils.config.SIGN_UP_BUTTON).click()

    def open_login(self):
        self.driver.find_element(By.XPATH, utils.config.LOG_IN_LINK).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, utils.config.LOG_IN_USER_NAME_FIELD)))

    def login(self, username, password):
        self.driver.find_element(By.ID, utils.config.LOG_IN_USER_NAME_FIELD).send_keys(username)
        self.driver.find_element(By.ID, utils.config.LOG_IN_PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(By.XPATH, utils.config.LOG_IN_BUTTON).click()

    def add_product_to_cart(self, product_name):
        product = self.driver.find_element(
            *self.product_1 if product_name == utils.config.PRODUCT_1 else self.product_2)
        product.click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, utils.config.ADD_TO_CART_BUTTON)))
        self.driver.find_element(By.CSS_SELECTOR, utils.config.ADD_TO_CART_BUTTON).click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present()).accept()

