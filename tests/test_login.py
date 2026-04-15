from selenium import webdriver
from pages.login_page import LoginPage
import os


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
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, "test_login_invalid_user.png")
        driver.save_screenshot(path)
        raise AssertionError("Login failed message is not displayed as expected.")




