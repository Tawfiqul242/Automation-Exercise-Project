from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.subscription_component import subscriptionComponent

class CartPage(BasePage):
    # page locators
    HOME_BTN = (By.XPATH, "//ol[@class='breadcrumb']//a[normalize-space()='Home']")
    FOOTER = (By.XPATH, "//footer[@id='footer']")
    CART_PRODUCTS_LIST = (By.XPATH, "//tr[contains(@id, 'product')]")
    CART_PRODUCTS_NAME = (By.XPATH, "//td[contains(@class,'cart_description')]//a")
    CART_PRODUCT_DETAILS = (By.TAG_NAME, "td")
    CART_PRODUCTS_PRICE = (By.XPATH, "//td[contains(@class,'cart_price')]//p")
    CART_PRODUCTS_QUANTITY = (By.XPATH, "//td[contains(@class,'cart_quantity')]//button")
    CART_PRODUCTS_TOTAL = (By.XPATH, "//td[contains(@class,'cart_total')]//p")


    def __init__(self, driver):
        super().__init__(driver)
        self.subscription = subscriptionComponent(driver)

    # page action methods
    def scroll_down_to_footer(self):
        self.scroller(self.FOOTER)

    def get_cart_products(self):
        products = self.wait_for_elements_visibility(self.CART_PRODUCTS_NAME)
        return [self.text_normalizer(product.text) for product in products]
    
    def get_prices(self):
        return [e.text for e in self.wait_for_elements_visibility(self.CART_PRODUCTS_PRICE )]

    def get_quantities(self):
        return [e.text for e in self.wait_for_elements_visibility(self.CART_PRODUCTS_QUANTITY)]

    def get_totals(self):
        return [e.text for e in self.wait_for_elements_visibility(self.CART_PRODUCTS_TOTAL)]




