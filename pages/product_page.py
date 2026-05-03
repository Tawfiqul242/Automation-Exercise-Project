from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    # page locators
    SEARCH_BAR = (By.CSS_SELECTOR, "#search_product")
    SEARCH_BAR_BTN = (By.CSS_SELECTOR, ".fa.fa-search")
    CATEGORY_TITLE = (By.XPATH, "//h2[normalize-space()='Category']")
    ALL_PRODUCT_TITLE = (By.CSS_SELECTOR, ".title.text-center")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    ADD_TO_CART_BTN = (By.XPATH, "(//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart'])[2]")
    VIEW_PRODUCT_BTN = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    SEARCHED_PRODUCT_TITLE = (By.XPATH, "//h2[normalize-space()='Searched Products']")

    def __init__(self, driver):
        super().__init__(driver)

    # page action methods
    def is_all_product_visible(self):
        return self.is_visible(self.ALL_PRODUCT_TITLE)
    
    def is_product_list_visible(self):
        return self.is_visible(self.PRODUCT_LIST)
    
    def click_add_to_cart_btn(self):
        self.click(self.ADD_TO_CART_BTN)

    def click_view_product_btn(self):
        self.click(self.VIEW_PRODUCT_BTN)

    def fill_search_bar(self, value):
        self.send_key(self.SEARCH_BAR, value)

    def click_search_btn(self):
        self.click(self.SEARCH_BAR_BTN)

    def is_searched_product_title_visible(self):
        return self.is_visible(self.SEARCHED_PRODUCT_TITLE)
    
    def get_all_product(self):
        products = self.wait_for_elements_visibility(self.PRODUCT_LIST)
  
        names = []
        for product in products:
            name = product.find_element(By.CSS_SELECTOR, ".productinfo p").text
            names.append(name)
    
        return names


    