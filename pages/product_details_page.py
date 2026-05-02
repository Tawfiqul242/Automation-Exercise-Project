from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductDetailsPage(BasePage):
    # page locators
    PRODUCT_NAME = (By.XPATH, "//h2[normalize-space()='Blue Top']")
    CATEGORY = (By.XPATH, "//p[normalize-space()='Category: Women > Tops']")
    PRICE = (By.XPATH, "//span[normalize-space()='Rs. 500']")
    AVAILABILITY = (By.XPATH, "//b[normalize-space()='Availability:']")
    CONDITION = (By.XPATH, "//b[normalize-space()='Condition:']")
    BRAND = (By.XPATH, "//b[normalize-space()='Brand:']")

    def __init__(self, driver):
        super().__init__(driver)

    #page action methods
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