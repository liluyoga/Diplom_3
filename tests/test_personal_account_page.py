import allure

from data import TestData
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:

    @allure.title("Переход по клику на Личный Кабинет")
    def test_crossing_personal_account(self, register_new_user, driver):
        user_data = register_new_user
        page = PersonalAccountPage(driver)
        page.personal_account_login(user_data.get("email"), user_data.get("password"))
        page.go_to_personal_account()
        actual_result = page.get_login_field_value()

        assert user_data.get("email") in actual_result

    @allure.title("Переход в раздел История заказов")
    def test_crossing_order_history(self, register_new_user, driver):
        user_data = register_new_user
        page = PersonalAccountPage(driver)
        page.personal_account_login(user_data.get("email"), user_data.get("password"))
        page.go_to_personal_account()
        page.go_to_order_history()
        actual_result = page.get_current_url()

        assert TestData.URL_ORDER_HISTORY in actual_result

    @allure.title("Выход из аккаунта")
    def test_exit_from_personal_account(self, register_new_user, driver):
        user_data = register_new_user
        page = PersonalAccountPage(driver)
        page.personal_account_login(user_data.get("email"), user_data.get("password"))
        page.go_to_personal_account()
        page.click_on_exit_button()

        assert page.check_login_button()
