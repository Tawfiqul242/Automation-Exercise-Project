from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.subscription_component import subscriptionComponent

class CartPage(BasePage):
    # page locators
    HOME_BTN = (By.XPATH, "//ol[@class='breadcrumb']//a[normalize-space()='Home']")
    FOOTER = (By.XPATH, "//footer[@id='footer']")

    def __init__(self, driver):
        super().__init__(driver)
        self.subscription = subscriptionComponent(driver)

    # page action methods
    def scroll_down_to_footer(self):
        self.scroller(self.FOOTER)



