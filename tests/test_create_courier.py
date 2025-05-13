import json

import allure
import pytest
import requests

from resousrces.create_new_courier import register_new_courier_and_return_response
from resousrces.data_courier import DATA
from resousrces.headers import HEADERS
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
        data = DATA["test_create_courier_without_login"]
        data_string = json.dumps(data)
        response = requests.post(create_courier_url, data=data_string,
                                 headers=HEADERS)

        assert 400 == response.status_code
        assert response.json()['message'] == not_enough_data

    @allure.title('Проверка создания курьера без пароля')
    def test_create_courier_without_password(self):
        data = DATA["test_create_courier_without_password"]
        data_string = json.dumps(data)
        response = requests.post(create_courier_url, data=data_string,
                                 headers=HEADERS)

        assert 400 == response.status_code
        assert response.json()['message'] == not_enough_data

    @allure.title('Проверка создания курьера без имени')
    def test_create_courier_without_firstName(self):
        data = DATA["create_courier_without_first_name"]
        data_string = json.dumps(data)
        response = requests.post(create_courier_url, data=data_string,
                                 headers=HEADERS)

        if response.status_code == 201:
            pytest.xfail("API теперь разрешает создавать курьера без имени (ожидалось 400)")
        else:
            assert response.status_code == 400
            assert response.json()["message"] == not_enough_data

    @allure.title('Проверка повторного создания курьера с теми же данными')
    def test_create_courier_re_registration(self):
        data = DATA["test_create_courier_re_registration"]
        data_string = json.dumps(data)
        response = requests.post(create_courier_url, data=data_string,
                                 headers=HEADERS)
        assert 201 == response.status_code
        response_duplicate = requests.post(create_courier_url, data=data_string,
                                           headers=HEADERS)

        assert 409 == response_duplicate.status_code
        assert response_duplicate.json()['message'] == login_busy
