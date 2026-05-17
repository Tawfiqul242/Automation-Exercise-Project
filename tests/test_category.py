import logging
from pages.home_page import HomePage
from pages.product_page import ProductPage

log = logging.getLogger(__name__)

def test_view_category_products(driver): # View Category Products Test
    # page class objects
    home = HomePage(driver)
    product = ProductPage(driver)

    log.info("--Starting View Category Products Test--")
    try:
        home.scroll_to_category()
        log.info("Scrolling to Category Section")

        # Verify that categories are visible on left side bar
        assert home.is_category_title_visible(), "Categories are not Visible"
        log.info("Categories are Visible")

        # Click on 'Women' category
        home.click_women_category()
        log.info("Clicked Women Category")

        # Click on any category link under 'Women' category
        home.select_women_sub_category("Dress")
        log.info("clicked Dress Sub Category under women category")

        # Verify that category page is displayed and confirm text 'WOMEN - DRESS PRODUCTS'
        assert product.is_sub_category_title_visible(), "Category page is not displayed"
        log.info("Category page is displayed")

        assert home.text_normalizer("WOMEN - DRESS PRODUCTS") in product.get_sub_category_text(), "Women - Dress Products text not available"
        log.info("Women - Dress Products text is available")

        # On left side bar, click on any sub-category link of 'Men' category
        home.click_men_category()
        log.info("Clicked Men Category")

        home.select_men_sub_category("Jeans")
        log.info("clicked Jeans Sub Category under men category")

        # Verify that user is navigated to that category page
        assert home.text_normalizer("MEN - JEANS PRODUCTS") in product.get_sub_category_text(), "Men - Jeans Products text is not visible"
        log.info("Men - Jeans Products is visible")

    except AssertionError as e:
        log.error(f"Test Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected Error: {e}")
        raise
    finally:
        log.info("--View Category Products Test Execution Finished--")


