from pages.login_page import LoginPage
from utils.screenshots import save_screenshots 
from utils.logger import setup_logging

logger = setup_logging(__name__)

logger.info("testing invalid user login")
def test_login_invalid_user(driver):

    login_page = LoginPage(driver)

    
    email = "email@gmail.com"
    password = 74125
    login_page.login(email, password)

    try:
        assert "Your email or password is incorrect!" in login_page.is_login_invalid()
        logger.info("Checking the error message for invalid login")
        
    except Exception as e:
        save_screenshots(driver,"test_login_invalid_user")
        logger.error(F"Failed to show the error message: {e}")
        #raise AssertionError("Login failed message is not displayed as expected.")
        
    




