import logging
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.product_details_page import ProductDetailsPage

log = logging.getLogger(__name__)

def test_all_products_detail_page(driver): # Verify All Products and product detail page
    # page class objects
    home = HomePage(driver)
    product = ProductPage(driver)
    product_details = ProductDetailsPage(driver)

    log.info("--Starting  All Products & Product Detail Page Test--")
    try:
        # Verify that home page is visible successfully
        home.is_homepage_visible(), "Home Page is not visible"
        log.info("Home Page is Visible")

        # Click on 'Products' button
        home.click_product_btn()
        log.info("Clicked Products Button")

        # Verify user is navigated to ALL PRODUCTS page successfully
        assert product.is_all_product_visible(), "User is not navigated to ALL PRODUCTS page"
        log.info("User is navigated to ALL PRODUCTS page")

        # The products list is visible
        assert product.is_product_list_visible(), "The products list is not visible"
        log.info("The products list is visible")

        # Click on 'View Product' of first product
        product.click_view_product_btn()
        log.info("clicked View Product button")

        # User is landed to product detail page
        assert product_details.is_product_name_visible(), "User is not landed to product detail page"
        log.info("User is landed to product detail page")

        # Verify that detail is visible: product name, category, price, availability, condition, brand
        assert product_details.is_product_name_visible(), "Product Name is not Visible"
        log.info("Product Name is Visible")

        assert product_details.is_category_visible(), "Product Category is not Visible"
        log.info("Product category is Visible")

        assert product_details.is_price_visible(), "Product price is not Visible"
        log.info("Product price is Visible")

        assert product_details.is_availability_visible(), "Product availability is not Visible"
        log.info("Product availability is Visible")

        assert product_details.is_condition_visible(), "Product condition is not Visible"
        log.info("Product condition is Visible")

        assert product_details.is_brand_visible(), "Product brand is not Visible"
        log.info("Product brand is Visible")


    except AssertionError as e:
        log.error(f"Assertion Failed:{e}") 
        raise

    except Exception as e:
        log.error(f"Unexpected error in test: {e}")
        raise

    finally:
        log.info("--All Products & Product Detail Page Test Execution Finished--")
