import logging
from pages.home_page import HomePage
from pages.test_case_page import CasePage

log = logging.getLogger(__name__)

def test_case_page(driver):
    #page class objects
    home = HomePage(driver)
    test_case = CasePage(driver)

    log.info("--Starting Test Cases Page Test--")

    try:
        # Verify that home page is visible successfully
        assert home.is_homepage_visible(), "Home Page is not Visible"
        log.info("Home page is visible successfully")

        #click test case button form navbar
        home.click_test_case_btn()
        log.info("Clicked Test Cases Button")

        # Verify user is navigated to test cases page successfully
        assert test_case.is_test_cases_visible(), "User is not navigated to test cases page"
        log.info("User is navigated to test cases page")

        log.info("Test Cases Page Test is Completed")

    except AssertionError as e:
        log.error(f"Test Cases Page Test Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected Error: {e}")
        raise
    finally:
        log.info("--Test Cases Page Test Execution Finished--")

 