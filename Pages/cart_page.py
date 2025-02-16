from selenium.webdriver.common.by import By
import utils.config

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_url = utils.config.CART_URL
        self.items_in_cart = (By.CSS_SELECTOR, utils.config.ITEMS_IN_THE_CART)
        self.item_names = (By.XPATH, utils.config.ITEM_NAMES)

    def open_cart(self):
        self.driver.get(self.cart_url)

    def get_cart_items(self):
        items = self.driver.find_elements(*self.items_in_cart)
        return [item.find_element(*self.item_names).text for item in items]
