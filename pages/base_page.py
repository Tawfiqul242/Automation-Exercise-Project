from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, timeout = 10): #constructor where driver & driver wait is initialized
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    
    def wait_for_element(self, locator):      #responsible for element's wait
        return self.wait.until(EC.visibility_of_element_located(locator)) 
    
    def click(self, locator):                 # responsible for clicking elements
        element = self.wait_for_element(locator)
        element.click()

    def send_key(self, locator, value):       # responsible for sending values
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):              # it will return messages
        element = self.wait_for_element(locator)
        return element.text