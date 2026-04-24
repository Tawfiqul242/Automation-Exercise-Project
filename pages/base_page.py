from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, timeout = 10): #constructor where driver & driver wait is initialized
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    
    def wait_for_element_visibility(self, locator):      #responsible for element's wait
        return self.wait.until(EC.visibility_of_element_located(locator)) 
    
    def click(self, locator):                 # responsible for clicking elements
        element = self.wait_for_element_visibility(locator)
        element.click()

    def send_key(self, locator, value):       # responsible for sending values
        element = self.wait_for_element_visibility(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):              # it will return messages
        element = self.wait_for_element_visibility(locator)
        return element.text
    
    def select_dropdown_by_value(self, locator, value): # it will select options from dropdown by value
        element = self.wait_for_element_visibility(locator)
        Select(element).select_by_value(value)

    def select_dropdown_by_visible_text(self, locator, value): # it will select option from dropdown by index
        element = self.wait_for_element_visibility(locator)
        Select(element).select_by_visible_text(value)

    def is_visible(self, locator):
        element = self.wait_for_element_visibility(locator)
        return element.is_displayed()