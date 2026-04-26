from faker import Faker
import random
import calendar
from pages.registration_page import RegistrationPage
from pages.account_info_page import AccountInfoPage

def generate_user_data(name = None, email = None):
    faker = Faker()
    random_number = random.randint(1000, 9999)
    random_day = random.randint(1, 31)
    random_month = random.randint(1,12)
    random_year = random.randint(1900, 2021)
    month = calendar.month_name[random_month]
    countrlylist = ["India","United States", "Canada", "Australia", "New Zealand", "Singapore"]
    country = random.choice(countrlylist)

    fname = faker.first_name()
    return{
        "name":name if name else fname,
        "email": email if email else f"{fname}{random_number}@gmail.com",
        "title": None,
        "password": f"{fname}{random_number}",
        "day": random_day,
        "month": month,
        "year": random_year,
        "newsletter": None,
        "offer": None,
        "fname": fname,
        "lname": faker.last_name(),
        "company": faker.company(),
        "address": faker.address(),
        "optional_address": None,
        "country": country,
        "state": faker.state(),
        "city": faker.city(),
        "zipcode": faker.zipcode(),
        "mobile": faker.msisdn()
    }

# Registered user helper
def register_new_user(driver, user_data):
    # page class objects
    signup = RegistrationPage(driver)
    account = AccountInfoPage(driver)

    signup.enter_signup_info(user_data) # fill signup form fields
    signup.click_signup()

    account.enter_account_info(user_data) #fill account information fields
    account.click_create_account()
