import requests
import random
import string

from resousrces.urls import create_courier_url


# Генерация случайной строки из букв нижнего регистра
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choices(letters, k=length))
    return random_string


# Регистрация нового курьера
def register_new_courier_and_return_response():
    # Генерация уникального логина, пароля и имени курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # Формирование тела запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # Отправка запроса на регистрацию курьера
    response = requests.post(create_courier_url, json=payload)

    return response
