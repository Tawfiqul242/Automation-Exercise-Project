from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):

    #locators
    NAME = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EMAIL_ADD = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    #SUCCESS_MESSAGE

    def __init__(self, driver):
        super().__init__(driver)
    
    def user_register(self, name, email):
        self.send_key(self.NAME, name)
        self.send_key(self.EMAIL_ADD, email)
        self.click(self.SIGNUP_BUTTON)

    
