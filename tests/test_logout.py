import logging
from pages.home_page import HomePage
from pages.login_page import LoginPage

log = logging.getLogger(__name__)

def test_logout_user(driver, logged_in_user_info):
    #page class objects
    home = HomePage(driver)
    login = LoginPage(driver)
    

    log.info("--Starting Logout user Test--")
    try:
        #Verify that home page is visible successfully
        assert home.is_homepage_visible(), "Home Page is not visible"
        log.info("Home Page is visible")

        #Click Signup?Login button
        home.click_signup_login_btn()
        log.info("Clicking Signup & Login button from navbar")

        #Verify 'Login to your account' is visible
        assert login.is_login_to_your_account_visible(), "'Login to your account' is not visible"
        log.info("'Login to your account' is visible")

        #filling login form with correct email address and password
        login.fill_login_form(logged_in_user_info)
        log.info("Filling login form")

        #Click 'login' button
        login.click_login()
        log.info("Clicking Login button")

        #Verify that 'Logged in as username' is visible
        assert login.is_logged_in_as_user_visible(), " 'Logged in as username' is not visible"
        log.info("'Logged in as username' is visible")

        # Click 'Logout' button
        home.click_logout_btn()
        log.info("Clicked logout button")

        #Verify that user is navigated to login page 
        assert login.is_login_to_your_account_visible(), "User is not vavigated to login page"
        log.info("user is navigated to login page ")

        log.info("Logout User Test is Completed")
    
    except AssertionError as e:
        log.error(f"Logout user Test Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected Error: {e}")
        raise
    finally:
        log.info("--Logout User Test Execution Finished--")

