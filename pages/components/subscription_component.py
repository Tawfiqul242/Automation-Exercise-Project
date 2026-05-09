from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class subscriptionComponent(BasePage):
    # locators
    SUBSCRIPTION_TITLE = (By.XPATH, "//h2[normalize-space()='Subscription']")
    SUBSCRIBE_EMAIL = (By.XPATH, "//input[@id='susbscribe_email']")
    SUBCRIBE_BUTTON = (By.XPATH, "//i[@class='fa fa-arrow-circle-o-right']")
    SUCCESS_MESSAGE = (By.ID, "success-subscribe")

    def __init__(self, driver):
        super().__init__(driver)

    #action methods
    def is_subscription_visible(self):
        return self.is_visible(self.SUBSCRIPTION_TITLE)
    
    def fill_email_field(self, email):
        self.send_key(self.SUBSCRIBE_EMAIL, email)

    def click_subscribe_btn(self):
        self.click(self.SUBCRIBE_BUTTON)

    def is_success_message_visible(self):
        return self.is_visible(self.SUCCESS_MESSAGE)
    

