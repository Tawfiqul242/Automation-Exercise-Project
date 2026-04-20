from pages.registration_page import RegistrationPage
from utils.screenshots import save_screenshots
from utils.logger import setup_logging

log = setup_logging(__name__)

def test_valid_user_register(driver):
    reg_page = RegistrationPage(driver)

    name = "hasu"
    email = "hasu@gmail.com"
    reg_page.user_register(name, email)

    try:
        assert "Enter Account Information" in reg_page.is_registration_successful()
        log.info("Registration Succuessfully Completed")

    except Exception as e:
        save_screenshots(driver, "Not successful register")
        log.error(f"Failed to signup: {e}")
        raise
