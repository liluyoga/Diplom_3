import allure

from locators.header_page_locators import HeaderPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Кликаем на Ленту заказов")
    def click_on_order_feed(self):
        self.click_on_element(HeaderPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликаем на Ленту заказов и на Заказ")
    def click_on_order_in_order_feed(self):
        self.click_on_element(HeaderPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element(OrderFeedPageLocators.ORDER)

    @allure.step("Проверка, что открылось всплывающее окно с деталями заказа")
    def check_modal_window_with_order_details_opened(self):
        if self.find_element_with_waiting(OrderFeedPageLocators.ORDER_DETAILS):
            return True

    @allure.step("Проверка, что номер заказа есть в Истории заказов и в Ленте заказов")
    def check_order_number_in_list(self, number):
        orders = self.find_all_elements_with_waiting(OrderFeedPageLocators.ORDERS_IN_HISTORY_AND_ORDER_FEED)
        for order in orders:
            if number in order.text:
                return True
            else:
                return False

    @allure.step("Проверка, что номер заказа есть в разделе В работе")
    def check_order_number_in_progress(self, number):
        self.wait_until_invisibility_element(OrderFeedPageLocators.LABEL_ALL_ORDERS_ARE_READY)
        order_locator = self.concat_locator_and_number(OrderFeedPageLocators.ORDER_LIST, number)
        if self.find_element_with_waiting(order_locator):
            return True
        else:
            return False

    @allure.step("Забираем количество выполненных заказов за всё время")
    def get_number_of_orders_all_time(self):
        number = self.get_text_from_element(OrderFeedPageLocators.COMPLETED_ORDERS_ALL_TIME_BEFORE)
        return number

    @allure.step("Забираем количество выполненных заказов за всё время после создания нового")
    def get_number_of_all_orders_after_create_new_order(self, number):
        old_locator = self.concat_locator_and_number(OrderFeedPageLocators.COMPLETED_ORDERS_ALL_TIME_FOR_FIND, number)
        self.wait_until_invisibility_element(old_locator)
        number = self.get_number_of_orders_today()
        return number

    @allure.step("Забираем количество выполненных заказов за сегодня")
    def get_number_of_orders_today(self):
        number = self.get_text_from_element(OrderFeedPageLocators.COMPLETED_ORDERS_TODAY_BEFORE)
        return number

    @allure.step("Забираем количество выполненных заказов за сегодня после создания нового")
    def get_number_of_orders_after_create_new_order(self, number):
        old_locator = self.concat_locator_and_number(OrderFeedPageLocators.COMPLETED_ORDERS_TODAY_FOR_FIND, number)
        self.wait_until_invisibility_element(old_locator)
        number = self.get_number_of_orders_today()
        return number
