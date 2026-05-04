import logging
from pages.home_page import HomePage
from pages.cart_page import CartPage

log = logging.getLogger(__name__)

def test_subscription_in_cart_page(driver):
    #page class objects
    home = HomePage(driver)
    cart = CartPage(driver)

    log.info("--Starting Subscription in Cart Page Test--")
    try:
        # Verify that home page is visible successfully
        assert home.is_homepage_visible(), "Home page is not visible successfully"
        log.info("Home page is visible successfully")

        # Click 'Cart' button
        home.click_cart_btn()
        log.info("Clicked Cart Button")

        # Scroll down to footer
        cart.scroll_down_to_footer()
        log.info("Scrolling down to footer section")

        # Verify text 'SUBSCRIPTION'
        assert cart.subscription.is_subscription_visible(), "'SUBSCRIPTION' is not visible"
        log.info("'SUBSCRIPTION' is visible")

        # Enter email address in input and click arrow button
        cart.subscription.fill_email_field("demo@gmailcom")
        log.info("Filling email address into the email field")

        # click subscribe button
        cart.subscription.click_subscribe_btn()
        log.info("clicked subscribe button")

        # Verify success message 'You have been successfully subscribed!' is visible
        assert cart.subscription.is_success_message_visible(), "'You have been successfully subscribed!' is not visible"
        log.info("'You have been successfully subscribed!' is visible")

    except AssertionError as e:
        log.error(f"Subscription In Cart Page Test Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected Error: {e}")
        raise
    finally:
        log.info("--Subscription In Cart Page Test Execution Finished--")
