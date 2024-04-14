import random


class TestData:
    URL_FORGOT_PASSWORD = '/forgot-password'
    URL_ORDER_HISTORY = '/account/order-history'

    USER_EMAIL = 'morty@yandex.ru'

    URL_API_REGISTER = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    URL_API_PLACE_ORDER = 'https://stellarburgers.nomoreparties.site/api/orders'
    URL_API_USER = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    URL_API_LOGIN = 'https://stellarburgers.nomoreparties.site/api/auth/login'

    @staticmethod
    def generate_new_user_data():
        user_data = {"email": f'morty{random.randint(0, 99)}@yandex.ru',
                     "password": f'{random.randint(100000, 999999)}',
                     "name": 'Морти'}
        return user_data

    order_data = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa6f",
            "61c0c5a71d1f82001bdaaa73"
        ]
    }
