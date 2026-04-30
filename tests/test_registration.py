from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.account_info_page import AccountInfoPage
from utils.screenshots import save_screenshots
import logging
from utils.logger import setup_logging
from utils.user_helper import generate_user_data
import time

log = logging.getLogger(__name__)

def test_valid_user_register(driver, new_user):  # test complete user registration account creations and deletation flow
    
    #page class objects
    home = HomePage(driver)
    signup = RegistrationPage(driver)
    account = AccountInfoPage(driver)

    try:
        log.info("--Starting User Registration Test--")

        #verify home page is visible and navigate to signup
        assert home.is_homepage_visible(), "Home page is not visible"
        log.info("Home Page is Visible")

        home.click_signup_login_btn()
        log.info("Clicking signup button from navbar")

        #verify "New User Singup" is visible
        assert signup.is_new_user_visible(), "New User Signup is not visible"
        log.info("New User Signup is visible")

        signup.enter_signup_info(new_user)
        log.info("Entered Name & Email in singup form")

        signup.click_signup()
        log.info("Clicking signup button")

        # Account Creation

        #verify "Enter Account Information" is visible
        assert account.is_enter_account_info_visible(), "Enter Account Information is not visible"
        log.info("Enter Account Information is visible")

        account.enter_create_account_info(new_user)
        log.info("Entered Account Information")
        account.click_create_account()
        log.info("clicking Create Account button")

        #verify "Account Created" is visible
        assert account.is_account_created_visible(), "Account Created is not visible"
        log.info("Account Created is visible")

        account.click_create_continue()
        log.info("Clicking Continue button")

        #verify user logged in is visible
        assert account.is_logged_in_visible(), "user logged in is not visible"
        log.info("User logged in is visible")

        #Account Deletation
        account.click_delete()
        log.info("Clicking Delete button")

        #verify "Account Deleted" is visible
        assert account.is_account_deleted_visible(), "Account Deleted is not visible"
        log.info("Account Deleted is visible")
        account.click_delete_continue()
        log.info("Clicking continue button")

        log.info("--Account Creation Completed--")

    except AssertionError as e:
        log.error(f"Assertion Failed: {e}")
        save_screenshots(driver, "Valid user registration test failure")
        raise

    except Exception as e:
        log.error(f"Unexpected error in test: {e}")
        save_screenshots(driver, "unexpected error")
        raise

    finally: 
        log.info("Valid User Account Creation Test Execution Finished.")



def test_register_user_with_existing_email(driver, registered_user): # Test- Register User with existing email 
    # page class objects
    home = HomePage(driver)
    signup = RegistrationPage(driver)

    log.info("--Starting Register User with Existing Email--")
    try:
        # Verify that home page is visible successfully
        assert home.is_homepage_visible(), "Home Page is not Visible"
        log.info("Home Page is Visible")

        #Click on 'Signup / Login' button
        home.click_signup_login_btn()
        log.info("Cliking Signup Login button")

        # Verify 'New User Signup!' is visible
        assert signup.is_new_user_visible(), "New User Signup is not Visible"
        log.info("New User Signup is visible")

        # Enter name and already registered email address
        signup.enter_signup_info(registered_user)
        log.info("Filling name and already registered email address")

        # Click 'Signup' button
        signup.click_signup()
        log.info("Clicked Signup Button")

        # Verify error 'Email Address already exist!' is visible 
        assert signup.is_email_already_exist(), "'Email Address already exist!' is not visible"
        log.info("'Email Address already exist!' is visible ")

        log.info("Register User with Existing Email Test is Completed")

    except AssertionError as e:
        log.error(f"Email address already exist! Test Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected Error: {e}")
        raise
    finally:
        log.info("--Register User with Existing Email Test Execution Finished--")
