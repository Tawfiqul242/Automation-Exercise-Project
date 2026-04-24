from faker import Faker
import random
import calendar

def generate_user_data(name = None, email = None):
    faker = Faker()
    random_number = random.randint(1000, 9999)
    random_day = random.randint(1, 31)
    random_year = random.randint(1900, 2021)
    month = calendar.month_name

    fname = faker.first_name()
    return{
        "name":name if name else fname,
        "email": email if email else f"{fname}{random_number}@gmail.com",
        "title": None,
        "password": f"{fname}{random_number}",
        "day": random_day,
        "month": random_month,
        "year": random_year,
        "newsletter": None,
        "offer": None,
        "fname": fname,
        "lname": faker.last_name(),
        "company": faker.company(),
        "address": faker.address(),
        "optional_address": None,
        "country": faker.country(),
        "state": faker.state(),
        "city": faker.city(),
        "zipcode": faker.zipcode(),
        "mobile": faker.msisdn()
    }