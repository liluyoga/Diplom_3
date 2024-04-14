import json

import allure
import requests

from data import TestData


@allure.step("Cоздание заказа")
def create_order_by_api(user_data):
    payload = {
        "email": user_data.get("email"),
        "password": user_data.get("password")
    }
    response = requests.post(TestData.URL_API_LOGIN, headers={"Content-type": "application/json"},
                             data=json.dumps(payload))
    token = response.json()["accessToken"]
    order = requests.post(TestData.URL_API_PLACE_ORDER,
                          headers={"Content-type": "application/json", "Authorization": f'{token}'},
                          data=json.dumps(TestData.order_data))
    number = order.json()["order"]["number"]
    return f'#0{number}'
