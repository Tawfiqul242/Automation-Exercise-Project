from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import os

class ContactUs(BasePage):
    # Page locators
    GET_IN_TOUCH = (By.XPATH, "//h2[normalize-space()='Get In Touch']")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='Name']")
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Email']")
    SUBJECT_FIELD = (By.XPATH, "//input[@placeholder='Subject']")
    MESSAGE_FIELD = (By.XPATH, "//textarea[@id='message']")
    UPLOAD_FILE = (By.XPATH, "//input[@name='upload_file']")
    SUBMIT_BTN = (By.XPATH, "//input[@name='submit']")
    FILE_UPLOAD_SUCCESS_MSG = (By.XPATH, "//div[@class='status alert alert-success']")
    HOME_BTN = (By.XPATH, "//span[normalize-space()='Home']")

    def __init__(self, driver):
        super().__init__(driver)

    # page action methods
    def is_get_in_touch_visible(self):
        return self.is_visible(self.GET_IN_TOUCH)
    
    def fill_get_in_touch_form(self, user_data):
        self.send_key(self.NAME_FIELD, user_data["name"])
        self.send_key(self.EMAIL_FIELD, user_data["email"])
        self.send_key(self.SUBJECT_FIELD, user_data["subject"])
        self.send_key(self.MESSAGE_FIELD, user_data["message"])

    def file_upload(self):
        file_input = self.wait_for_element_visibility(self.UPLOAD_FILE)
        file_path = os.path.abspath("test_data/DemoFileUpload.txt")
        file_input.send_keys(file_path)

    def click_ok_btn(self):
        self.handle_alert()

    def is_file_upload_success_msg_visible(self):
        return self.is_visible(self.FILE_UPLOAD_SUCCESS_MSG)
    

    def click_submit_btn(self):
        self.click(self.SUBMIT_BTN)

    def click_home_btn(self):
        self.click(self.HOME_BTN)

