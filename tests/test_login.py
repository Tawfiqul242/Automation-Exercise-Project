from selenium import webdriver
from pages.login_page import LoginPage
from utils.screenshots import save_screenshots 


def test_login_invalid_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationexercise.com/login")

    login_page = LoginPage(driver)

    
    email = "email@gmail.com"
    password = 74125
    login_page.login(email, password)

    try:
        assert "Your email or password is incorrect!" in login_page.is_login_invalid()
        
    except:
        save_screenshots(driver,"test_login_invalid_user")
        raise AssertionError("Login failed message is not displayed as expected.")




