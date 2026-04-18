import pytest
from selenium import webdriver
from utils.screenshots import save_screenshots
from utils.logger import setup_logging

print("CONFTEST FILE LOADED")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationexercise.com/login")

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
    print("LOGGING FIXTURE RUNNING")  # debug
    setup_logging()