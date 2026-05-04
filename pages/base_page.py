from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, timeout = 10): #constructor where driver & driver wait is initialized
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    
    def wait_for_element_visibility(self, locator):      #responsible for single element's wait
        return self.wait.until(EC.visibility_of_element_located(locator)) 
    
    def wait_for_elements_visibility(self, locator):      #responsible for multiple element's wait
        return self.wait.until(EC.visibility_of_all_elements_located(locator)) 
    
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

    def is_visible(self, locator):   # it will return displayed element
        element = self.wait_for_element_visibility(locator)
        return element.is_displayed()
    
    def handle_alert(self, action = "accept"): # It will handle browser alert
        alert = self.wait.until(EC.alert_is_present())

        if action == "accept":
            alert.accept()
        else:
            alert.dismiss() 

    def text_normalizer(self,text): # It will remove " ", -, _ from a text
        return text.lower().replace(" ", "").replace("-", "").replace("_", "")
    
    def scroller(self, locator): # it willl scroll through the web page
        element = self.wait_for_element_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)