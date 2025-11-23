import random
import allure
from faker import Faker

fake = Faker('ru_RU')

@allure.step('Генерируем новый случайный пароль')
def password_generator():
    generated_password = fake.random_number(6)
    return str(generated_password)

@allure.step('Генерируем новый случайный email')
def email_generator():
    generated_email = fake.email()
    return generated_email

@allure.step('Генерируем новое случайное имя')
def first_name_generator():
    generate_name = fake.first_name()
    return generate_name