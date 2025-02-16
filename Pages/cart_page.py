from selenium.webdriver.common.by import By
import utils.config

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_url = utils.config.CART_URL
        self.items_in_cart = (By.CSS_SELECTOR, utils.config.ITEMS_IN_THE_CART)
        self.item_names = (By.XPATH, utils.config.ITEM_NAMES)

        self.place_order_btn = (By.XPATH, utils.config.PLACE_ORDER_BUTTON)
        self.name_input = (By.ID, utils.config.PLACE_ORDER_NAME)
        self.country_input = (By.ID, utils.config.PLACE_ORDER_COUNTRY)
        self.city_input = (By.ID, utils.config.PLACE_ORDER_CITY)
        self.card_input = (By.ID, utils.config.PLACE_ORDER_CARD)
        self.month_input = (By.ID, utils.config.PLACE_ORDER_MONTH)
        self.year_input = (By.ID, utils.config.PLACE_ORDER_YEAR)
        self.purchase_btn = (By.XPATH, utils.config.PURCHASE_BUTTON)

    def open_cart(self):
        self.driver.get(self.cart_url)

    def get_cart_items(self):
        items = self.driver.find_elements(*self.items_in_cart)
        return [item.find_element(*self.item_names).text for item in items]

    def open_order_modal(self):
        self.driver.find_element(*self.place_order_btn).click()

    def fill_checkout_form(self):
        self.driver.find_element(*self.name_input).send_keys(utils.config.PURCHASE_VALUE_NAME)
        self.driver.find_element(*self.country_input).send_keys(utils.config.PURCHASE_VALUE_COUNTRY)
        self.driver.find_element(*self.city_input).send_keys(utils.config.PURCHASE_VALUE_CITY)
        self.driver.find_element(*self.card_input).send_keys(utils.config.PURCHASE_VALUE_CARD)
        self.driver.find_element(*self.month_input).send_keys(utils.config.PURCHASE_VALUE_MONTH)
        self.driver.find_element(*self.year_input).send_keys(utils.config.PURCHASE_VALUE_YEAR)

    def confirm_purchase(self):
        self.driver.find_element(*self.purchase_btn).click()