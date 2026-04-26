import pytest
from selenium import webdriver
from utils.screenshots import save_screenshots
from utils.logger import setup_logging
import logging
from utils.user_helper import generate_user_data
from utils.user_helper import register_new_user

#Initialize logging for once for the entire test session
@pytest.fixture(scope="session", autouse= True)
def setup_project_logging():
    setup_logging("test_session")
    log =logging.getLogger(__name__) 
    log.info("Project logging initalized successfully at session level")

    yield  
    log.info("Shutting down logging")                        
    logging.shutdown()
    log.info("Logging shut down complete.")

#Driver fixtue for function level
@pytest.fixture(scope= "function")
def driver():
    log = logging.getLogger(__name__)

    log.info("Starting Chrome Browser")
    driver = webdriver.Chrome()
    driver.maximize_window()
    log.info("Navigating to URL: https://automationexercise.com/")
    driver.get("https://automationexercise.com/")

    yield driver
    
    log.info("Quitting Browser")
    driver.quit()
    log.info("Browser closed successfully")

#Capture screeenshots automatically on test failure.
@pytest.hookimpl(hookwrapper = True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    log = logging.getLogger(__name__)

    if report.when=="call" and report.failed:
        driver = item.funcargs.get("driver", None)

        try:
            if driver:
                save_screenshots(driver, item.name)
                log.info("Screenshot capture for failed test: {item.name}")
        except Exception as e:
            log.info("Failed to take screenshot for {item.name}: {e}")

#user data generator fixture for function level
@pytest.fixture(scope="function")
def new_user():
    log = logging.getLogger(__name__)

    log.info("New user data is generating")
    user_data = generate_user_data()

    log.info("New user data is ready to be used")
    return user_data

# registered user fixture for function level
@pytest.fixture(scope="function")
def registered_user(driver, new_user):
    log = logging.getLogger(__name__)

    log.info("Registering new user")
    register_new_user(driver, new_user) # register new user

    log.info("New user registration completed")
    return new_user


