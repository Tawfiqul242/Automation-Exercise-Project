from selenium.webdriver.common.by import By 
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class AccountInfoPage(BasePage):
    #locators
    MR_TITLE = (By.CSS_SELECTOR, "label[for='id_gender1']")
    MRS_TITLE =  (By.CSS_SELECTOR, "label[for='id_gender2']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    BIRTH_DAY_DROPDWON = Select((By.CSS_SELECTOR, "#days"))
    BIRTH_MONTH_DROPDOWN = Select((By.CSS_SELECTOR, "#months"))
    BIRTH_YEAR_DROPDOWN = Select((By.CSS_SELECTOR, "#years"))
    NEWSLETTER_CHECKBOX = (By.CSS_SELECTOR, "#newsletter")
    OFFERS_CHECKBOX = (By.CSS_SELECTOR, "#option")
    FIRST_NAME = (By.CSS_SELECTOR, "#first_name")
    LAST_NAME = (By.CSS_SELECTOR, "#last_name")
    COMPANY = (By.CSS_SELECTOR, "#company")
    ADDRESS =(By.CSS_SELECTOR, "#address1")
    OPTIONAL_ADDRESS = (By.CSS_SELECTOR, "#address2")
    COUNTRY = (By.CSS_SELECTOR, "#country")
    STATE = (By.CSS_SELECTOR, "#state")
    CITY = (By.CSS_SELECTOR, "#city")
    ZIPCODE = (By.CSS_SELECTOR, "#zipcode")
    MOBILE_NUMBER = (By.CSS_SELECTOR, "#mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")

    def __init__(self, driver):
        super().__init__(driver)

    

