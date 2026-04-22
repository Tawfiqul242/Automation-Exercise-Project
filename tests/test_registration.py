from pages.registration_page import RegistrationPage
from utils.screenshots import save_screenshots
from utils.logger import setup_logging
from utils.user_helper import generate_user
import time

log = setup_logging(__name__)

def test_valid_user_register(driver):
    reg_page = RegistrationPage(driver)

    user_data = generate_user()
    reg_page.user_register(user_data)


    try:
        assert "Enter Account Information" in reg_page.is_registration_successful()
        log.info("Registration Succuessfully Completed")

    except Exception as e:
        save_screenshots(driver, "Not successful register")
        log.error(f"Failed to signup: {e}")
        raise
