from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.account_info_page import AccountInfoPage
from utils.screenshots import save_screenshots
from utils.logger import setup_logging
from utils.user_helper import generate_user
import time

log = setup_logging(__name__)

def test_valid_user_register(driver):
    user_data = generate_user()
    """  user_info = {
        "title": "Mr.",
        "password": "raf123",
        "day": "20",
        "month": 11,
        "year": "2001",
        "newsletter": "yes",
        "offer": "yes",
        "fname": "Rafin",
        "lname": "Hasan",
        "company": "RH",
        "address": "Uttara, Dhaka",
        "optional_address": "Dakkhin Khan",
        "country": 5,
        "state": "Dhaka",
        "city": "dhaka",
        "zipcode": "1230",
        "mobile": "01484813242"
    } """
    
    home = HomePage(driver)
    signup = RegistrationPage(driver)
    account = AccountInfoPage(driver)


    assert home.is_homepage_visible()
    home.click_signup()
    assert signup.is_new_user_visible()
    signup.enter_signup_info(user_data)
    time.sleep(5)
    signup.click_signup()
    assert account.is_enter_account_info_visible()
    account.enter_create_account_info(user_data)
    time.sleep(10)
    account.click_create_account()
    assert account.is_account_created_visible()
    account.click_create_continue()
    assert account.is_logged_in_visible()
    account.click_delete()
    assert account.is_account_deleted_visible()
    account.click_delete_continue()


