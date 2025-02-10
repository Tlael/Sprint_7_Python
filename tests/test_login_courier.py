import json

import allure
import requests

from resousrces.data_courier import DATA
from resousrces.headers import HEADERS
from resousrces.message import profile_not_found, without_login_or_password
from resousrces.urls import login_courier_url


class TestLoginCourier:
    @allure.title('Проверка логина курьера')
    def test_login_courier(self):
        data = DATA["test_login_courier"]
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=HEADERS)
        assert 200 == response.status_code
        assert 'id' in response.json()

    @allure.title('Проверка логина курьера с неверным паролем')
    def test_login_courier_incorrect_pass(self):
        data = DATA["test_login_courier_incorrect_pass"]
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=HEADERS)
        assert 404 == response.status_code
        assert response.json()['message'] == profile_not_found

    @allure.title('Проверка логина курьера без логина')
    def test_login_courier_without_login(self):
        data = DATA["test_login_courier_without_login"]
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=HEADERS)
        assert 400 == response.status_code
        assert response.json()['message'] == without_login_or_password

    @allure.title('Проверка логина курьера без пароля')
    def test_login_courier_without_password(self):
        data = DATA["test_login_courier_without_password"]
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=HEADERS)
        assert 400 == response.status_code
        assert response.json()['message'] == without_login_or_password

    @allure.title('Проверка логина несуществующего курьера')
    def test_login_courier_not_found(self):
        data = DATA["test_login_courier_not_found"]
        data_string = json.dumps(data)
        response = requests.post(login_courier_url, data=data_string,
                                 headers=HEADERS)
        assert 404 == response.status_code
        assert response.json()['message'] == profile_not_found
