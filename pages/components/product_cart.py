from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class ProductCart(BasePage):
    # locators
    PRODUCT_LIST = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[normalize-space()='Continue Shopping']")
    VIEW_CART_BTN = (By.XPATH, "//u[normalize-space()='View Cart']")

    def __init__(self, driver):
        super().__init__(driver)

    # methods
    def hover_over_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def add_product_by_index(self, index):
        products = self.wait_for_elements_visibility(self.PRODUCT_LIST)
        product = products[index]
        self.hover_over_element(product)
        add_btn = product.find_element(By.CSS_SELECTOR, ".overlay-content a")
        self.driver.execute_script("arguments[0].click();", add_btn)
    
    def click_continure_shopping_btn(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def click_view_cart_btn(self):
        self.click(self.VIEW_CART_BTN)
