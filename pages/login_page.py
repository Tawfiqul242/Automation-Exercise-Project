from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger import setup_logging

log = setup_logging(__name__)

class LoginPage(BasePage):

    #page locator
    LOGIN_TO_YOUR_ACCOUNT = (By.XPATH, "//h2[normalize-space()='Login to your account']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[placeholder='Password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGGED_IN_AS_USER =(By.CSS_SELECTOR, "li:nth-child(10) a:nth-child(1)")
    LOGIN_FAIL_MESSAGE = (By.CSS_SELECTOR, "body > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(2) > p:nth-child(4)")
    DELETE_ACCOUNT_BTN = (By.CSS_SELECTOR, "a[href='/delete_account']")
    ACCOUNT_DELETED = (By.CSS_SELECTOR, "h2[class='title text-center'] b")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    
    # page methods
    #"Login to your account" headline visibility
    def is_login_to_your_account_visible(self):
        return self.is_visible(self.LOGIN_TO_YOUR_ACCOUNT)

    # fill up the login form
    def fill_login_form(self, user_data):
        self.send_key(self.EMAIL_FIELD, user_data["email"])
        self.send_key(self.PASSWORD_FIELD, user_data["password"])
        
    #clicking login button
    def click_login(self):
        self.click(self.LOGIN_BTN)

    #logged in as user is visibility
    def is_logged_in_as_user_visible(self):
        return self.is_visible(self.LOGGED_IN_AS_USER)
    
    #click delete button
    def click_delete(self):
        self.click(self.DELETE_ACCOUNT_BTN)

    #"Account Deleted" visibility
    def is_account_deleted_visible(self):
        return self.is_visible(self.ACCOUNT_DELETED)

    #show validation error message
    def is_login_invalid(self):
        return self.get_text(self.LOGIN_FAIL_MESSAGE)

