import allure

from helper import create_order_by_api
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeedPage:

    @allure.title("При клике на заказ открывается всплывающее окно с деталями")
    def test_order_details(self, driver):
        page = OrderFeedPage(driver)
        MainPage(driver).click_on_order_feed_button()
        page.click_on_order_in_order_feed()

        assert page.check_modal_window_with_order_details_opened()

    @allure.title("Заказы пользователя из раздела История заказов отображаются в Ленте заказов")
    def test_order_from_order_history_in_order_feed(self, create_order, driver):
        user_data = create_order[0]
        number = create_order[1]
        page = OrderFeedPage(driver)
        authorization = PersonalAccountPage(driver)
        authorization.personal_account_login(user_data.get("email"), user_data.get("password"))
        authorization.go_to_personal_account()
        authorization.go_to_order_history()
        MainPage(driver).click_on_order_feed_button()

        assert page.check_order_number_in_list(number)

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_increase_counter_all_time_orders(self, register_new_user, driver):
        user_data = register_new_user
        page = OrderFeedPage(driver)
        MainPage(driver).click_on_order_feed_button()
        counter_before = page.get_number_of_orders_today()
        create_order_by_api(user_data)
        counter_after = page.get_number_of_orders_today()

        assert counter_after > counter_before

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_increase_counter_today_orders(self, register_new_user, driver):
        user_data = register_new_user
        page = OrderFeedPage(driver)
        MainPage(driver).click_on_order_feed_button()
        counter_before = page.get_number_of_orders_today()
        create_order_by_api(user_data)
        counter_after = page.get_number_of_orders_today()

        assert counter_after > counter_before

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_in_progress(self, register_new_user, driver):
        user_data = register_new_user
        page = OrderFeedPage(driver)
        authorization = PersonalAccountPage(driver)
        authorization.personal_account_login(user_data.get("email"), user_data.get("password"))
        number = create_order_by_api(user_data)
        MainPage(driver).click_on_order_feed_button()

        assert page.check_order_number_in_progress(number[2:]), f'Заказ в работе отсутствует'
