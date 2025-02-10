import json

import allure
import pytest
import requests

from resousrces import data_orders
from resousrces.headers import HEADERS
from resousrces.urls import get_orders_url


class TestCreateOrder:
    @allure.title('Проверка создания заказа на самокаты')
    @pytest.mark.parametrize('color',
                             [
                                 data_orders.ORDER_NO_COLOR,
                                 data_orders.ORDER_COLOR_BLACK,
                                 data_orders.ORDER_COLOR_GREY,
                                 data_orders.ORDER_COLOR_BLACK_AND_GREY
                             ])
    def test_create_order(self, color):
        data_string = json.dumps(color)
        response = requests.post(get_orders_url, data=data_string, headers=HEADERS)
        assert 201 == response.status_code
        assert 'track' in response.json()
