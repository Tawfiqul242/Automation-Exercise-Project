from pages.registration_page import RegistrationPage
#from pages.account_info_page import AccountInfoPage
from utils.screenshots import save_screenshots
from utils.logger import setup_logging
from utils.user_helper import generate_user
import time

log = setup_logging(__name__)

def test_valid_user_register(driver):
    reg_page = RegistrationPage(driver)

    user_data = generate_user()
    user_info = {
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
    }
    create_account = reg_page.user_register(user_data)
    #time.sleep(6)
    create_account.account_create(user_info) 
    #time.sleep(10)

    try:
        assert "account created!" in reg_page.is_registration_successful().lower()
        log.info("Registration Succuessfully Completed")

    except Exception as e:
        save_screenshots(driver, "Not successful register")
        log.error(f"Failed to signup: {e}")
        raise
