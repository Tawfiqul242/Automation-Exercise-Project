from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.components.subscription_component import subscriptionComponent
from pages.components.product_cart import ProductCart

class HomePage(BasePage):
    #locators
    HOME_BTN = (By.XPATH, "//a[normalize-space()='Home']")
    SIGNUP_LOGIN_BTN = (By.CSS_SELECTOR, "a[href='/login']")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a[href='/logout']")
    PRODUCTS_BTN = (By.CSS_SELECTOR, "a[href='/products']")
    CART_BTN = (By.XPATH, "//body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]")
    TEST_CASES_BTN = (By.XPATH, "//a[contains(text(),'Test Cases')]")
    API_TESTING_BTN = (By.XPATH, "//a[normalize-space()='API Testing']")
    cONTACT_US_BTN = (By.XPATH, "//a[normalize-space()='Contact us']")
    SUBSCRIPTION_TITLE = (By.XPATH, "//h2[normalize-space()='Subscription']")
    FOOTER = (By.XPATH, "//footer[@id='footer']")
    PRODUCT_LIST = (By.XPATH, "//div[@class='features_items']")
    VIEW_PRODUCT_BTN = (By.XPATH, "(//div[@class='choose']//ul//li//a")
    FEATURE_ITEMS_TITLE = (By.XPATH, "//h2[normalize-space()='Features Items']")
    DELETE_BTN = (By.XPATH, "//a[normalize-space()='Delete Account']")
    ACCOUNT_DELETED = (By.CSS_SELECTOR, "h2[class='title text-center'] b")
    DELETE_CONTINUE_BTN = (By.XPATH, "//a[normalize-space()='Continue']")


    def __init__(self, driver):
        super().__init__(driver)
        self.subscription = subscriptionComponent(driver)
        self.product_cart = ProductCart(driver)
    
    #page action methods
    def is_homepage_visible(self):
        return "automation exercise" in self.driver.title.lower()
    
    def click_signup_login_btn(self):
        self.click(self.SIGNUP_LOGIN_BTN)

    def click_logout_btn(self):
        self.click(self.LOGOUT_BTN)

    def click_home_btn(self):
        self.click(self.HOME_BTN)

    def click_contact_us_btn(self):
        self.click(self.cONTACT_US_BTN)

    def click_test_case_btn(self):
        self.click(self.TEST_CASES_BTN)

    def click_product_btn(self):
        self.click(self.PRODUCTS_BTN)

    def click_cart_btn(self):
        self.click(self.CART_BTN)

    def scroll_to_footer(self):
        self.scroller(self.FOOTER)

    def scroll_to_feature_items(self):
        self.scroller(self.FEATURE_ITEMS_TITLE)

    def click_view_product_btn(self):
        products = self.wait_for_elements_visibility(self.PRODUCT_LIST)
        view_btn = products[0].find_element(By.XPATH, ".//a[contains(text(),'View Product')]")
        self.driver.execute_script("arguments[0].click();", view_btn)

    def click_delete_btn(self):
        self.click(self.DELETE_BTN)

    def is_account_deleted_visible(self):
        return self.is_visible(self.ACCOUNT_DELETED)

    def click_delete_continue(self):
        self.click(self.DELETE_CONTINUE_BTN)

        