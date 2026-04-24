from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.account_info_page import AccountInfoPage

class RegistrationPage(BasePage):

    #locators
    NEW_USER_SIGNUP = (By.CSS_SELECTOR, "div[class='signup-form'] h2")
    NAME = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EMAIL_ADD = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def __init__(self, driver):
        super().__init__(driver)
    
    #page action
    def is_new_user_visible(self):
        return self.is_visible(self.NEW_USER_SIGNUP)
    
    def enter_signup_info(self, user_data):
        self.send_key(self.NAME, user_data["name"])
        self.send_key(self.EMAIL_ADD, user_data["email"])
        
    def click_signup(self):
        self.click(self.SIGNUP_BUTTON)
        #return AccountInfoPage(self.driver)

 

    

    
