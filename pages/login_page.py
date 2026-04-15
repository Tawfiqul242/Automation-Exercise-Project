from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    #page locator
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_FAIL_MESSAGE = (By.CSS_SELECTOR, "body > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(2) > p:nth-child(4)")

    # page methods
    def login(self, email, password):
        self.send_key(self.EMAIL_FIELD, email)
        self.send_key(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_invalid(self):
        return self.get_text(self.LOGIN_FAIL_MESSAG)

