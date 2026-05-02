from selenium.webdriver.common.by import By
from pages.base_page import BasePage

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

    def __init__(self, driver):
        super().__init__(driver)
    
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