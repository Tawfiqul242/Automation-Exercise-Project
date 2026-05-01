import logging
from pages.home_page import HomePage
from pages.contact_us_page import ContactUs

log = logging.getLogger(__name__)

def test_contact_us_form(driver, new_user):
    # page class objects
    home = HomePage(driver)
    contact = ContactUs(driver)

    log.info("--Satring Contact Us Form Test--")

    try:
        # Verify that home page is visible successfully
        assert home.is_homepage_visible(), "Home Page is not Visible"
        log.info("Home page is visible successfully")

        home.click_contact_us_btn()
        log.info("Clicking Contact Us button")

        # Verify 'GET IN TOUCH' is visible
        assert contact.is_get_in_touch_visible(), "'GET IN TOUCH' is not visible"
        log.info("'GET IN TOUCH' is visible")

        # Enter name, email, subject and message
        contact.fill_get_in_touch_form(new_user)
        log.info("Filling Contact Us Form Fields")

        #Upload file
        contact.file_upload()
        log.info("Uploading the file")

        # Click 'Submit' button
        contact.click_submit_btn()
        log.info("Clicked Submit Button")

        # Click OK button
        contact.handle_alert()
        log.info("Clicked Ok in browser alert")

        # Verify success message 'Success! Your details have been submitted successfully.' is visible
        contact.is_file_upload_success_msg_visible(), "File upload success message is not visible"
        log.info("File upload success message is visible")

        #click Home button
        contact.click_home_btn()
        log.info("Clicked Home Button")

        # verify that landed to home page successfully
        assert home.is_homepage_visible(), "Landed to Home Page Successfully"

        log.info("Contact Us Form Test Completed")
    
    except AssertionError as e:
        log.error(f"Contact Us Form Test Failed: {e}")
        raise
    except Exception as e:
        log.error(f"Unexpected Error: {e}")
        raise
    finally:
        log.info("--Contact Us Form Test Execution Finished--")
