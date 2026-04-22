from faker import Faker
import random

def generate_user(name = None, email = None):
    faker = Faker()
    random_number = random.randint(1000, 9999)

    return{
        "name":name if name else faker.first_name(),
        "email": email if email else f"user{random_number}@gmail.com"
    }