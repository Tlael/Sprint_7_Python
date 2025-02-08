import allure
import requests
from resousrces.urls import get_orders_url


class TestOrders:
    @allure.title('Проверка получения списка заказов')
    def test_get_orders(self):
        response = requests.get(get_orders_url)
        assert 200 == response.status_code
        assert 'orders' in response.json()
