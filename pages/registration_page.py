from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.account_info_page import AccountInfoPage

class RegistrationPage(BasePage):

    #locators
    NAME = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EMAIL_ADD = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "h2[class='title text-center'] b")

    def __init__(self, driver):
        super().__init__(driver)
    
    #page action
    def user_register(self, user_data):
        self.send_key(self.NAME, user_data["name"])
        self.send_key(self.EMAIL_ADD, user_data["email"])
        self.click(self.SIGNUP_BUTTON)
        return AccountInfoPage(self.driver)

    def is_registration_successful(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    

    
