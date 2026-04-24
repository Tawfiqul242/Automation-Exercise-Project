from selenium.webdriver.common.by import By 
from pages.base_page import BasePage

class AccountInfoPage(BasePage):
    #locators
    ENTER_ACCOUNT_INFO = (By.XPATH, "//b[normalize-space()='Enter Account Information']")
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
    ACCOUNT_CREATED = (By.CSS_SELECTOR, "h2[class='title text-center'] b")
    CREATE_CONTINUE_BTN = (By.XPATH, "//a[normalize-space()='Continue']")
    LOGGED_IN_TEXT = (By.CSS_SELECTOR, "li:nth-child(10) a:nth-child(1)")
    DELETE_ACCOUNT_BTN = (By.CSS_SELECTOR, "a[href='/delete_account']")
    ACCOUNT_DELETED = (By.CSS_SELECTOR, "h2[class='title text-center'] b")
    DELETE_CONTINUE_BTN = (By.XPATH, "//a[normalize-space()='Continue']")

    def __init__(self, driver):
        super().__init__(driver)

    #page action methods
    def is_enter_account_info_visible(self):
        return self.is_visible(self.ENTER_ACCOUNT_INFO)
    
    def enter_account_info(self, title, password, day, month, year):
        self.click(self.MR_TITLE) if title == "Mr." else self.click(self.MRS_TITLE)
        self.send_key(self.PASSWORD_FIELD, password)
        self.select_dropdown_by_value(self.BIRTH_DAY, str(day))
        self.select_dropdown_by_visible_text(self.BIRTH_MONTH, str(month))
        self.select_dropdown_by_visible_text(self.BIRTH_YEAR, str(year))
        
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


    def enter_create_account_info(self, user_info):
        self.enter_account_info(
            user_info["title"],
            user_info["password"],
            user_info["day"],
            user_info["month"],
            user_info["year"]
            )
        
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

    def click_create_account(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created_visible(self):
        return self.is_visible(self.ACCOUNT_CREATED)
    
    def click_create_continue(self):
        self.click(self.CREATE_CONTINUE_BTN)

    def is_logged_in_visible(self):
        return self.is_visible(self.LOGGED_IN_TEXT)
    
    def click_delete(self):
        self.click(self.DELETE_ACCOUNT_BTN)
    
    def is_account_deleted_visible(self):
        return self.is_visible(self.ACCOUNT_DELETED)

    def click_delete_continue(self):
        self.click(self.DELETE_CONTINUE_BTN)

