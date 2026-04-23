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

    def select_title(self, title):
        self.click(self.MR_TITLE) if title == "Mr." else self.click(self.MRS_TITLE)

    def enter_password(self, password):
        self.send_key(self.PASSWORD_FIELD, password)

    def enter_birthdate(self, day, month, year):
        self.BIRTH_DAY_DROPDWON.select_by_value(day)
        self.BIRTH_MONTH_DROPDOWN.select_by_index(month)
        self.BIRTH_YEAR_DROPDOWN.select_by_value(year)

    def select_newsletter(self, newsletter = None):
        if newsletter: self.click(self.NEWSLETTER_CHECKBOX)

    def select_offers(self, offer = None):
        if offer: self.click(self.OFFERS_CHECKBOX)

    def enter_address(self,user_info):
        

    def account_create(self, title, password, birthDay,birthMonth, birthYear, newsletter, offers, fName, lName, country, state, city, zipcode, contact):
        self.click(self.OFFERS_CHECKBOX)

