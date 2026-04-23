from selenium.webdriver.common.by import By 
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class AccountInfoPage(BasePage):
    #locators
    MR_TITLE = (By.CSS_SELECTOR, "label[for='id_gender1']")
    MRS_TITLE =  (By.CSS_SELECTOR, "label[for='id_gender2']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    BIRTH_DAY= (By.CSS_SELECTOR, "#days")
    BIRTH_MONTH = (By.CSS_SELECTOR, "#months")
    BIRTH_YEAR = (By.CSS_SELECTOR, "#years")
    NEWSLETTER_CHECKBOX = (By.CSS_SELECTOR, "#newsletter")
    OFFERS_CHECKBOX = (By.CSS_SELECTOR, "#optin")
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

    #page action methods

    def select_title(self, title):
        self.click(self.MR_TITLE) if title == "Mr." else self.click(self.MRS_TITLE)

    def enter_password(self, password):
        self.send_key(self.PASSWORD_FIELD, password)

    def enter_birth_day(self, value):
        self.select_dropdown_by_value(self.BIRTH_DAY, value)

    def enter_birth_month(self, value):
        self.select_dropdown_by_index(self.BIRTH_MONTH, value)

    def enter_birth_year(self, value):
        self.select_dropdown_by_value(self.BIRTH_YEAR, value)

    def select_newsletter(self, newsletter = None):
        if newsletter: self.click(self.NEWSLETTER_CHECKBOX)

    def select_offers(self, offer = None):
        if offer: self.click(self.OFFERS_CHECKBOX)

    def enter_address(self, fname, lname, company, address, optional_address, country, state, city, zipcode, mobile):
        self.send_key(self.FIRST_NAME, fname)
        self.send_key(self.LAST_NAME, lname)
        self.send_key(self.COMPANY, company)
        self.send_key(self.ADDRESS, address)
        self.send_key(self.OPTIONAL_ADDRESS, optional_address)
        self.select_dropdown_by_index(self.COUNTRY, country)
        self.send_key(self.STATE, state)
        self.send_key(self.CITY, city)
        self.send_key(self.ZIPCODE, zipcode)
        self.send_key(self.MOBILE_NUMBER, mobile)


    def account_create(self, user_info):
        self.select_title(user_info["title"])
        self.enter_password(user_info["password"])
        
        self.enter_birth_day(user_info["day"])
        self.enter_birth_month(user_info["month"])
        self.enter_birth_year(user_info["year"])
        
        self.select_newsletter(user_info["newsletter"])
        self.select_offers(user_info["offer"])
       
        self.enter_address(
            user_info["fname"],
            user_info["lname"],
            user_info["company"],
            user_info["address"],
            user_info["optional_address"],
            user_info["country"],
            user_info["state"],
            user_info["city"],
            user_info["zipcode"],
            user_info["mobile"],
        )
        self.click(self.CREATE_ACCOUNT_BUTTON)

