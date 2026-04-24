import pytest
from selenium import webdriver
from utils.screenshots import save_screenshots
from utils.logger import setup_logging
import logging

print("CONFTEST FILE LOADED")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationexercise.com/")

    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper = True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when=="call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            save_screenshots(driver, item.name)


@pytest.fixture(scope="session", autouse= True)
def setup_project_logging():
    setup_logging("test_session")
    print("LOGGING FIXTURE RUNNING")  # debug
    yield                           # this line is the key addition
    logging.shutdown()