from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.components.subscription_component import subscriptionComponent

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
    SHOPPING_CART_TITLE = (By.XPATH, "//li[@class='active']")
    ITEM_REMOVE_BTN = (By.XPATH, "//td[contains(@class,'cart_delete')]//a")
    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[normalize-space()='Proceed To Checkout']")
    CHECKOUT_LOGIN_SIGNUP_BTN = (By.XPATH, "//u[normalize-space()='Register / Login']")
    CART_IS_EMPTY_TITLE = (By.XPATH, "//b[normalize-space()='Cart is empty!']")


    def __init__(self, driver):
        super().__init__(driver)
        self.subscription = subscriptionComponent(driver)

    # page action methods
    def is_shopping_cart_visible(self):
        return self.is_visible(self.SHOPPING_CART_TITLE)
    
    def scroll_down_to_footer(self):
        self.scroller(self.FOOTER)

    def is_product_visible(self):
        return self.is_visible(self.CART_PRODUCT_DETAILS)

    def get_cart_products(self):
        products = self.wait_for_elements_visibility(self.CART_PRODUCTS_NAME)
        return [self.text_normalizer(product.text) for product in products]
    
    def get_prices(self):
        return [e.text for e in self.wait_for_elements_visibility(self.CART_PRODUCTS_PRICE )]

    def get_quantities(self):
        return [e.text for e in self.wait_for_elements_visibility(self.CART_PRODUCTS_QUANTITY)]

    def get_totals(self):
        return [e.text for e in self.wait_for_elements_visibility(self.CART_PRODUCTS_TOTAL)]
    
    def get_remove_btn(self):
        return [e for e in self.wait_for_elements_visibility(self.ITEM_REMOVE_BTN)]
    
    def is_product_removed(self, product_name):
        products = self.get_cart_products()
        for product in products:
            if product_name in product:
                return False
        return True
    
    def click_proceed_to_checkout_btn(self):
        self.click(self.PROCEED_TO_CHECKOUT)

    def click_signin_signup_btn(self):
        self.click(self.CHECKOUT_LOGIN_SIGNUP_BTN)




