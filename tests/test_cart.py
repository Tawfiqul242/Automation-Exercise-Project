import time
import logging
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage

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

def test_product_quantity_in_cart(driver):
    #page class objects
    home = HomePage(driver)
    cart = CartPage(driver)
    product_detail = ProductDetailsPage(driver)

    target_quantity = 4

    log.info("--Starting Subscription in Cart Page Test--")
    try:
        # Verify that home page is visible successfully
        assert home.is_homepage_visible(), "Home page is not visible successfully"
        log.info("Home page is visible successfully")

        # scroll to feature items
        home.scroll_to_feature_items()
        log.info("Scrolling to feature items")

        # Click 'View Product' for any product on home page
        home.click_view_product_btn()
        log.info("Clicked View Product Button")

        # Verify product detail is opened
        assert product_detail.is_product_details_visible(), "Product details is not opened"
        log.info("Product details is opened")

        # Increase quantity to 4
        product_detail.increase_product_qty(target_quantity)
        log.info(f"Increasing product quantity to {target_quantity}")

        # Click 'Add to cart' button
        product_detail.click_add_to_cart_btn()
        log.info("Clicked Add to Cart Button")

        # Click 'View Cart' button
        product_detail.click_view_cart_btn()
        log.info("Clicked View Cart Button")

        # Verify that product is displayed in cart page with exact quantity
        assert cart.is_product_visible(), "Product is not displayed"
        log.info("Product is displayed")

        qty_list = cart.get_quantities()
        assert int(qty_list[0]) == target_quantity, "Quantity is not exact"
        log.info("Quantity is exact")

    except AssertionError as e:
        log.error(f"Product Quantity In Cart Test Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected Error: {e}")
        raise
    finally:
        log.info("--Product Quantity In Cart Test Execution Finished--")


def test_remove_products_from_cart(driver): # Remove Products From Cart Test
    #page class objects
    home = HomePage(driver)
    cart = CartPage(driver)

    log.info("--Starting Remove Products From Cart Test--")
    try:
        # Verify that home page is visible successfully
        assert home.is_homepage_visible(), "Home page is not visible successfully"
        log.info("Home page is visible successfully")

        # scroll to feature items
        home.scroll_to_feature_items()
        log.info("Scrolling to feature items")

        # Add products to cart
        home.product_cart.add_product_by_index(0)
        home.product_cart.click_continure_shopping_btn()
        log.info("Clicked add to cart of first product & clicked continue shopping button")

        # Click 'Cart' button
        home.click_cart_btn()
        log.info("Clicked Cart button from navbar")

        # Verify that cart page is displayed
        cart.is_shopping_cart_visible(), "Cart page is not displayed"
        log.info("Cart page is displayed")

        # Click 'X' button corresponding to particular product
        remove_btn = cart.get_remove_btn()
        cart.click(remove_btn[0])

        # Verify that product is removed from the cart
        assert cart.is_cart_is_empty_title_visible(), "Product is not removed from the cart"
        log.info("Product is removed from the cart")

    except AssertionError as e:
        log.error(f"Product Quantity In Cart Test Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected Error: {e}")
        raise
    finally:
        log.info("--Remove Products From Cart Test Execution Finished--")

