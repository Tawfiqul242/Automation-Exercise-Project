from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    #locators
    DELIVERY_ADDRESS = (By.XPATH, "//ul[@id='address_delivery']")
    BILLING_ADDRESS = (By.XPATH, "//ul[@id='address_invoice']")
    PRODUCT_NAME = (By.XPATH, "//td[@class='cart_description']//a")
    PRODUCT_PRICE = (By.XPATH, "//td[@class='cart_price']//p")
    PRODUCT_QUANTITY = (By.XPATH, "//td[@class='cart_quantity']//button")
    PRODUCT_TOTAL = (By.XPATH, "//td[@class='cart_total']//p")
    DESCRIPTION_TEXT = (By.XPATH, "//textarea[@name='message']")
    PLACE_ORDER_BTN = (By.XPATH, "//a[normalize-space()='Place Order']")

    def __init__(self, driver):
        super().__init__(driver)

    # page methods
    def is_delivery_address_visible(self):
        return self.is_visible(self.DELIVERY_ADDRESS)
    
    def is_billing_address_visible(self):
        return self.is_visible(self.BILLING_ADDRESS)
    
    def get_ordered_products(self):
        names = self.wait_for_elements_visibility(self.PRODUCT_NAME)
        prices = self.wait_for_elements_visibility(self.PRODUCT_PRICE)
        qty = self.wait_for_elements_visibility(self.PRODUCT_QUANTITY)
        total = self.wait_for_elements_visibility(self.PRODUCT_TOTAL)
        products = []

        for i in range(len(names)):
            products.append(
                {
                    "name": self.text_normalizer(names[i].text),
                    "price": self.text_normalizer(prices[i].text),
                    "qty": self.text_normalizer(qty[i].text),
                    "total": self.text_normalizer(total[i].text)
                }
            )
        return products
    
    def write_comment(self):
        self.send_key(self.DESCRIPTION_TEXT, "Testing...")

    def click_place_order_btn(self):
        self.click(self.PLACE_ORDER_BTN)


    