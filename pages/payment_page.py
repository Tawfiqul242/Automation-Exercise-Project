from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class PaymentPage(BasePage):
    # page locators
    CARD_NAME = (By.XPATH, "//input[@name='name_on_card']")
    CARD_NUMBER = (By.XPATH, "//input[@name='card_number']")
    CVC = (By.XPATH, "//input[@placeholder='ex. 311']")
    EXPIRATION_MONTH = (By.XPATH, "//input[@placeholder='MM']")
    EXPIRATION_YEAR = (By.XPATH, "//input[@placeholder='YYYY']")
    PAY_CONFIRM_ORDER_BTN = (By.XPATH, "//button[@id='submit']")
    PAYMENT_SUCCESS_MESSAGE = (By.XPATH, "//b[normalize-space()='Order Placed!']")

    def __init__(self, driver):
        super().__init__(driver)

    #page methods
    def fill_payment_info(self, payment_info):
        self.send_key(self.CARD_NAME,payment_info["card_name"])
        self.send_key(self.CARD_NUMBER,payment_info["card_number"])
        self.send_key(self.CVC,payment_info["cvc"])
        self.send_key(self.EXPIRATION_MONTH,payment_info["month"])
        self.send_key(self.EXPIRATION_YEAR,payment_info["year"])
    
    def click_pay_confirm_order(self):
        self.click(self.PAY_CONFIRM_ORDER_BTN)
    
    def is_order_success_message_visible(self):
        return self.is_visible(self.PAYMENT_SUCCESS_MESSAGE)