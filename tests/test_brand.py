import logging
import time
from pages.home_page import HomePage
from pages.product_page import ProductPage

log = logging.getLogger(__name__)

def test_view_and_cart_brand_products(driver): # View & Cart Brand Products Test
    # page class objects
    home = HomePage(driver)
    product = ProductPage(driver)

    log.info("--Starting View & Cart Brand Products Test--")

    # Click on 'Products' button
    home.click_product_btn()
    log.info("Clicked Product Button from navabar")

    home.scroll_to_brand()

    # Verify that Brands are visible on left side bar
    assert home.is_brand_title_visible(), "Brand Title is not visible"
    log.info("Brand Title is visible")

    assert home.are_brands_visilbe(), "Brands are not visible"
    log.info("Brands are visible")

    # Click on any brand name
    home.select_brand("Polo")
    log.info("Brand Polo Selected")
    time.sleep(5)

    # Verify that user is navigated to brand page and brand products are displayed
    assert home.text_normalizer("Brand - Polo Products") in product.get_sub_category_or_brand_text(), "Not navigated to polo brand page"
    log.info("Navigated to polo brand page")

    assert product.are_products_visible(), "Polo brand products are not displayed"
    log.info("Polo brand products are displayed")

    # On left side bar, click on any other brand link
    home.select_brand("H&M")
    log.info("Brand H&M Selected")

    # Verify that user is navigated to that brand page and can see products
    assert home.text_normalizer("Brand - H&M Products") in product.get_sub_category_or_brand_text(), "Not navigated to H&M brand page"
    log.info("Navigated to H&M brand page")

    assert product.are_products_visible(), "H&M Brand Products are not displayed"
    log.info("H&M Brand Products are displayed")

    log.info("--View & Cart Brand Products Test Execution Finished--")