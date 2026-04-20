import logging
from pages.login_page import LoginPage
from utils.screenshots import save_screenshots 
from utils.logger import setup_logging
 
log = setup_logging(__name__)

def test_login_invalid_user(driver):
    log.info("testing invalid user login")
    login_page = LoginPage(driver)

    
    email = "emailgmail.com"
    password = 74125
    login_page.login(email, password)

    try:
        assert "Your email or password is incorrect!" in login_page.is_login_invalid()
        log.info("Checking the error message for invalid login")
        
    except Exception as e:
        save_screenshots(driver,"test_login_invalid_user")
        log.error(f"Failed to show the error message: {e}")
        raise
        
    




