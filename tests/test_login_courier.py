import json

import allure
import requests

from resousrces.message import profile_not_found, without_login_or_password
from resousrces.urls import login_courier_url


class TestLoginCourier:
    @allure.title('Проверка логина курьера')
    def test_login_courier(self):
        data = {
            "login": "pavlova_18",
            "password": "1234"
        }
        headers = {"Content-type": "application/json"}
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=headers)
        assert 200 == response.status_code
        assert 'id' in response.json()

    @allure.title('Проверка логина курьера с неверным паролем')
    def test_login_courier_incorrect_pass(self):
        data = {
            "login": "pavlova_18",
            "password": "4321"
        }
        headers = {"Content-type": "application/json"}
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=headers)
        assert 404 == response.status_code
        assert response.json()['message'] == profile_not_found

    @allure.title('Проверка логина курьера без логина')
    def test_login_courier_without_login(self):
        data = {
            "password": "4321"
        }
        headers = {"Content-type": "application/json"}
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=headers)
        assert 400 == response.status_code
        assert response.json()['message'] == without_login_or_password

    @allure.title('Проверка логина курьера без пароля')
    def test_login_courier_without_password(self):
        data = {
            "password": "4321"
        }
        headers = {"Content-type": "application/json"}
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=headers)
        assert 400 == response.status_code
        assert response.json()['message'] == without_login_or_password

    @allure.title('Проверка логина несуществующего курьера')
    def test_login_courier_not_found(self):
        data = {
            "login": "ruiwrow",
            "password": "rwioeerk"
        }
        headers = {"Content-type": "application/json"}
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=headers)
        assert 404 == response.status_code
        assert response.json()['message'] == profile_not_found
