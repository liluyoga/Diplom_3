import allure

from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestMainPage:

    @allure.title("Проверка, что клик на ингредиент вызывает всплывающее окно с деталями")
    def test_ingredient_details(self, driver):
        page = MainPage(driver)
        page.click_on_ingredient()
        result = page.check_modal_window_with_details

        assert result

    @allure.title("Проверка закрытия всплывающего окна с деталями")
    def test_close_ingredient_details(self, driver):
        page = MainPage(driver)
        page.click_on_ingredient()
        page.click_close_ingredient_details()

        assert page.check_modal_windows_with_details_closed

    @allure.title("Проверка увеличения счётчика ингредиента при добавлении его в заказ")
    def test_ingredient_counter(self, driver):
        page = MainPage(driver)
        counter_before = page.check_ingredient_counter()
        page.move_ingredient_to_basket()
        counter_after = page.check_ingredient_counter()

        assert counter_after > counter_before

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_place_order_by_authorized_user(self, register_new_user, driver):
        user_data = register_new_user
        page = MainPage(driver)
        authorization = PersonalAccountPage(driver)
        authorization.personal_account_login(user_data.get("email"), user_data.get("password"))
        page.move_ingredient_to_basket()
        page.click_place_order_button()

        assert page.check_order_placed
