import logging
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.account_info_page import AccountInfoPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from utils.user_helper import card_info

log = logging.getLogger(__name__)
try:
    def test_register_while_checkout(driver, new_user): #Place Order: Register while Checkout
        #page class objects
        home = HomePage(driver)
        register = RegistrationPage(driver)
        account = AccountInfoPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)
        payment = PaymentPage(driver)

        log.info("--Sarting Place Order: Register while Checkout Test--")

        # Verify that home page is visible successfully
        assert home.is_homepage_visible(), "Home page is not visible"
        log.info("Home page is visible successfully")

        # Add products to cart
        home.scroll_to_feature_items()
        log.info("Scrolling to features items")
    
        home.product_cart.add_product_by_index(0)
        log.info("Clicked Add to Cart Button")

        # Click 'Cart' button
        home.product_cart.click_view_cart_btn()
        log.info("Clicked  View Cart Button")

        # Verify that cart page is displayed
        assert cart.is_shopping_cart_visible(), "Cart page is not displayed"
        log.info("Cart page is displayed")

        # Click Proceed To Checkout
        cart.click_proceed_to_checkout_btn()
        log.info("Clicked Proceed To Checkout Button")

        # Click 'Register / Login' button
        cart.click_signin_signup_btn()
        log.info("Clicked PRegister/Login Button")

        # Fill all details in Signup and create account
        register.enter_signup_info(new_user)
        register.click_signup()
        log.info("Filling Register Form & Clicked Signup Button")
        account.enter_create_account_info(new_user)
        account.click_create_account()

        # Verify 'ACCOUNT CREATED!' and click 'Continue' button
        assert account.is_account_created_visible(), "Account Created is not Visible"
        account.click_create_continue()
        log.info("Account Created is Visible & Clicked Continue Button")

        # Verify ' Logged in as username' at top
        assert account.is_logged_in_visible(), "Logged in as not username"
        log.info("Logged in as username")

        # Click 'Cart' button
        home.click_cart_btn()
        log.info("Clicked Cart Button form Navbar")

        # Click 'Proceed To Checkout' button
        cart.click_proceed_to_checkout_btn()
        log.info("Clicked 'Proceed To Checkout' button")

        # Verify Address Details and Review Your Order
        assert checkout.is_delivery_address_visible(), "Address details is not visible"
        log.info("Address details is visible")

        products = checkout.get_ordered_products()
        cart_total = 0
        for i in range(len(products)):
            assert products[i]["name"] == checkout.text_normalizer("Blue Top"), "Product Name is not correct"
            log.info("Product Name is correct")
        
            assert products[i]["price"] == checkout.text_normalizer("500"), "Product Price is not correct"
            log.info("Product Price is correct")

            assert products[i]["qty"] == checkout.text_normalizer("1"), "Product Quantity is not correct"
            log.info("Product Quantity is correct")
        
            cart_total += int(products[i]["total"])
    
        assert cart_total == 500, "Product Total is not correct"
        log.info("Product Total is correct")

        # Enter description in comment text area and click 'Place Order'
        checkout.write_comment()
        checkout.click_place_order_btn()
        log.info("Enter description in comment text area and click 'Place Order' button")

        # Enter payment details: Name on Card, Card Number, CVC, Expiration date
        payment.fill_payment_info(card_info())
        log.info("Filling Payment Info")

        # Click 'Pay and Confirm Order' button
        payment.click_pay_confirm_order()
        log.info("Clicked 'Pay and Confirm Order' button")

        """ #Verify success message 'Your order has been placed successfully!'
        assert payment.is_order_success_message_visible(), "'Your order has been placed successfully!' is not visible"
        log.info("Success Message is Visible") """

        #Click 'Delete Account' button
        home.click_delete_btn()
        log.info("Clicked Delete Button")

        # Verify 'ACCOUNT DELETED!' and click 'Continue' button
        assert home.is_account_deleted_visible(), "'ACCOUNT DELETED!' is not visible"
        log.info("'ACCOUNT DELETED!' is visible")

        home.click_delete_continue()
        log.info("Clicked Continue Button")

except AssertionError as e:
    log.error(f"Assertion Failed:{e}") 
    raise

except Exception as e:
    log.error(f"Unexpected error in test: {e}")
    raise

finally:
    log.info("--Place Order: Register while Checkout Test Execution Finished--")




