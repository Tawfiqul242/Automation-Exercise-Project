from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    #locators
    HOME_BTN = (By.XPATH, "//a[normalize-space()='Home']")
    SIGNUP_LOGIN_BTN = (By.CSS_SELECTOR, "a[href='/login']")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a[href='/logout']")

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