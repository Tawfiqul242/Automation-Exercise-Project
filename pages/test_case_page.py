from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CasePage(BasePage):
    # page locators
    TEST_CASES_HEADER = (By.XPATH, "//b[normalize-space()='Test Cases']")

    def __init__(self, driver):
        super().__init__(driver)

    # page action methods
    def is_test_cases_visible(self):
        return self.is_visible(self.TEST_CASES_HEADER)
    