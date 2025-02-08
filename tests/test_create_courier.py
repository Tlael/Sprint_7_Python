import json

import allure
import requests

from resousrces.create_new_courier import register_new_courier_and_return_response
from resousrces.message import not_enough_data, login_busy
from resousrces.urls import create_courier_url


class TestCreateCourier:
    @allure.title('Проверка создания курьера')
    def test_create_courier(self):
        response = register_new_courier_and_return_response()
        assert 201 == response.status_code
        assert response.json()['ok'] == True

    @allure.title('Проверка создания курьера без логина')
    def test_create_courier_without_login(self):
        data = {
            "password": "1234",
            "firstName": "saske"
        }
        headers = {"Content-type": "application/json"}
        data_string = json.dumps(data)
        response = requests.post(create_courier_url, data=data_string,
                                 headers=headers)

        assert 400 == response.status_code
        assert response.json()['message'] == not_enough_data

    @allure.title('Проверка создания курьера без пароля')
    def test_create_courier_without_password(self):
        data = {
            "login": "ninja",
            "firstName": "saske"
        }
        headers = {"Content-type": "application/json"}
        data_string = json.dumps(data)
        response = requests.post(create_courier_url, data=data_string,
                                 headers=headers)

        assert 400 == response.status_code
        assert response.json()['message'] == not_enough_data

    @allure.title('Проверка создания курьера без имени')
    def test_create_courier_without_firstName(self):
        data = {
            "login": "ninja",
            "password": "1234",
        }
        headers = {"Content-type": "application/json"}
        data_string = json.dumps(data)
        response = requests.post(create_courier_url, data=data_string,
                                 headers=headers)

        assert 400 == response.status_code
        assert response.json()['message'] == not_enough_data

    @allure.title('Проверка повторного создания курьера с теми же данными')
    def test_create_courier_re_registration(self):
        data = {
            "login": "pavlova_32",
            "password": "1234",
            "firstName": "saske"
        }
        headers = {"Content-type": "application/json"}
        data_string = json.dumps(data)
        response = requests.post(create_courier_url, data=data_string,
                                 headers=headers)
        assert 201 == response.status_code
        response_duplicate = requests.post(create_courier_url, data=data_string,
                                           headers=headers)

        assert 409 == response_duplicate.status_code
        assert response_duplicate.json()['message'] == login_busy
