import logging
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.account_info_page import AccountInfoPage
 
log = logging.getLogger(__name__)

def test_login_user_with_valid_data(driver, registered_user): # test login with valid credentials
    # page class objects
    login = LoginPage(driver)
    home = HomePage(driver)
    account = AccountInfoPage(driver)
    
    log.info("--Starting login with valid credentials test")
    try:
        #verify home page is visible
        assert home.is_homepage_visible(), "Home page is not visible"
        log.info("Home page is visible")

        home.click_signup_login_btn()
        log.info("cliciing signup/login button from navbar")

        #verify "Log in to your account" is visible
        assert login.is_login_to_your_account_visible(), "Log in to your account is not visible"
        log.info("Login to your account is visible")

        login.fill_login_form(registered_user)
        login.click_login()
        log.info("Clicking login button")

        #verify "Logged in user name is visible"
        assert login.is_logged_in_as_user_visible(), "Logged in as user is not visible"
        log.info("Logged in as user is visible")

        account.click_delete()
        log.info("Clicking Delete button")

        #verify "Account Deleted is visible"
        assert account.is_account_deleted_visible(), "Account Deleted is not visible"
        log.info("Account Deleted is visible")

        log.info("--Login with valid credentials test is completed")

    except AssertionError as e:
        log.error(f"Assertion Failed:{e}") 
        raise

    except Exception as e:
        log.error(f"Unexpected error in test: {e}")
        raise

    finally:
        log.info("--Login With Valid Data Test Execution Finished--")
        
    



def test_login_user_with_invalid_data(driver, new_user): # test login with invalid credentials
    #page objects
    login = LoginPage(driver)
    home = HomePage(driver)

    try:
        log.info("-- Starting Login User With Invalid Data Test--")

        #Verify home page is visible
        assert home.is_homepage_visible(), "Home page is not visible"
        log.info("Home page is visible")

        home.click_signup_login_btn()
        log.info("Clicking Signup/Login button from navbar")

        # Verify 'Login to your account' is visible
        assert login.is_login_to_your_account_visible(), "Login to your account is not visible"
        log.info("Login to your account is visible")

        # Enter incorrect email address and password
        login.fill_login_form(new_user)
        log.info("Filling invalid data into login form")

        #Click 'login' button
        login.click_login()
        log.info("Clicking Login button")

        # Verify error 'Your email or password is incorrect!' is visible
        assert login.is_email_password_incorrect_visible(), "'Your email or password is incorrect!' is not visible"
        log.info("'Your email or password is incorrect!' is visible")

        log.info("--Login User With Invalid Data Test is Completed--")

    except AssertionError as e:
        log.error(f"Assertion Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected error: {e}")
        raise
    finally:
        log.info("--Login User With Invalid Data Test Execution Finished--")



