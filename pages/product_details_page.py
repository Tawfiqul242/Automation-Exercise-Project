from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ProductDetailsPage(BasePage):
    # page locators
    PRODUCT_DETAILS  = (By.XPATH, "//div[@class='product-details']")
    PRODUCT_NAME = (By.XPATH, "//h2[normalize-space()='Blue Top']")
    CATEGORY = (By.XPATH, "//p[normalize-space()='Category: Women > Tops']")
    PRICE = (By.XPATH, "//span[normalize-space()='Rs. 500']")
    QUANTITY = (By.XPATH, "//input[@id='quantity']")
    AVAILABILITY = (By.XPATH, "//b[normalize-space()='Availability:']")
    CONDITION = (By.XPATH, "//b[normalize-space()='Condition:']")
    BRAND = (By.XPATH, "//b[normalize-space()='Brand:']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[normalize-space()='Add to cart']")
    VIEW_CART_BTN = (By.XPATH, "//u[normalize-space()='View Cart']")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[normalize-space()='Continue Shopping']")

    def __init__(self, driver):
        super().__init__(driver)

    #page action methods
    def is_product_details_visible(self):
        return self.is_visible(self.PRODUCT_DETAILS)

    def is_product_name_visible(self):
        return self.is_visible(self.PRODUCT_NAME)
    
    def is_category_visible(self):
        return self.is_visible(self.CATEGORY)
    
    def is_price_visible(self):
        return self.is_visible(self.PRICE)
    
    def is_availability_visible(self):
        return self.is_visible(self.AVAILABILITY)
    
    def is_condition_visible(self):
        return self.is_visible(self.CONDITION)
    
    def is_brand_visible(self):
        return self.is_visible(self.BRAND)
    
    def increase_product_qty(self, target):
        element = self.wait_for_element_visibility(self.QUANTITY)
        for i in range(target-1):
            element.send_keys(Keys.ARROW_UP)

    def click_add_to_cart_btn(self):
        self.click(self.ADD_TO_CART_BTN)

    def click_view_cart_btn(self):
        add_btn = self.wait_for_element_visibility(self.VIEW_CART_BTN)
        self.driver.execute_script("arguments[0].click();", add_btn)

    def click_continure_shopping_btn(self):
        self.click(self.CONTINUE_SHOPPING_BTN)