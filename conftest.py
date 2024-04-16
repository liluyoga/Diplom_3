import json

import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FirefoxOption

from data import TestData
from helper import generate_new_user_data, create_order_by_api


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--headless', default='false', help='headless options: "true" or "false"')


@pytest.fixture
@allure.title(f'Запуск драйвера')
def driver(request):
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')

    if browser == 'firefox':
        firefox_option = FirefoxOption()
        if headless == 'true':
            firefox_option.add_argument('--headless')
            firefox_option.add_argument('--ignore-certificate-errors')
            firefox_option.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=firefox_option)
    elif browser == 'chrome':
        chrome_option = ChromeOption()
        if headless == 'true':
            chrome_option.add_argument('--headless')
        chrome_option.add_argument('--ignore-certificate-errors')
        chrome_option.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_option)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    driver.get(TestData.URL)
    yield driver
    driver.quit()


@allure.step("Генерация и регистрация нового пользователя")
@pytest.fixture(scope='function')
def register_new_user():
    user_data = generate_new_user_data()
    response = requests.post(TestData.URL_API_REGISTER, headers={"Content-type": "application/json"},
                             data=json.dumps(user_data))
    token = response.json()["accessToken"]
    yield user_data
    requests.delete(TestData.URL_API_USER, headers={"Authorization": f'{token}'})


@allure.step("Создание заказа авторизованным пользователем")
@pytest.fixture(scope='function')
def create_order(register_new_user):
    user_data = register_new_user
    number = create_order_by_api(user_data)

    return user_data, number
