import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Кликаем на ссылку Личный Кабинет")
    def click_on_personal_account(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step("Клик на Конструктор")
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на Ленту заказов")
    def click_on_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Проверяем переход в Конструктор бургера")
    def check_burger_constructor_page(self):
        return self.find_element_with_waiting(MainPageLocators.LABEL_BUILD_BURGER)

    @allure.step("Проверяем переход в Ленту заказов")
    def check_order_feed_page(self):
        return self.find_element_with_waiting(MainPageLocators.LABEL_ORDER_FEED)

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)

    @allure.step("Клик по крестику закрытия деталей")
    def click_close_ingredient_details(self):
        self.click_on_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS)

    @allure.step("Проверка деталей ингредиента во всплывающем окне")
    def check_modal_window_with_details(self):
        return self.find_element_with_waiting(MainPageLocators.LABEL_INGREDIENT_DETAILS)

    @allure.step("Подтверждение закрытия всплывающего окна с деталями")
    def check_modal_windows_with_details_closed(self):
        if not self.wait_until_invisibility_element(MainPageLocators.MODAL_OPENED):
            return True
        else:
            return False

    @allure.step("Перетаскивание ингредиента в корзину")
    def move_ingredient_to_basket(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.BURGER_BASKET)

    @allure.step("Проверка счётчика ингредиента")
    def check_ingredient_counter(self):
        counter = self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)
        return counter

    @allure.step("Клик на кнопку Оформить заказ")
    def click_place_order_button(self):
        self.click_on_element(MainPageLocators.BUTTON_PLACE_ORDER)

    @allure.step("Проверка оформления заказа")
    def check_order_placed(self):
        if self.find_element_with_waiting(MainPageLocators.ORDER_PLACED):
            return True
