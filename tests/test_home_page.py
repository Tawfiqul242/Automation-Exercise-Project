import logging
from pages.home_page import HomePage

log = logging.getLogger(__name__)

def test_subscription_in_home_page(driver):
    #page class objects
    home = HomePage(driver)

    log.info("--Starting Subscription in Home Page Test--")
    try:
        # Verify that home page is visible successfully
        assert home.is_homepage_visible(), "Home page is not visible successfully"
        log.info("Home page is visible successfully")
        
        # Scroll down to footer
        home.scroll_to_footer()
        log.info("Scrolling down to footer section")

        # Verify text 'SUBSCRIPTION'
        assert home.subscription.is_subscription_visible(), "'SUBSCRIPTION' is not visible"
        log.info("'SUBSCRIPTION' is visible")

        # Enter email address in input and click arrow button
        home.subscription.fill_email_field("demo@gmailcom")
        log.info("Filling email address into the email field")

        # click subscribe button
        home.subscription.click_subscribe_btn()
        log.info("clicked subscribe button")

        # Verify success message 'You have been successfully subscribed!' is visible
        assert home.subscription.is_success_message_visible(), "'You have been successfully subscribed!' is not visible"
        log.info("'You have been successfully subscribed!' is visible")

    except AssertionError as e:
        log.error(f"Subscription In Home Page Test Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected Error: {e}")
        raise
    finally:
        log.info("--Subscription In Home Page Test Execution Finished--")
