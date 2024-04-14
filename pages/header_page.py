import allure

from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step("Кликаем на ссылку Личный Кабинет в хедере страницы")
    def click_on_personal_account(self):
        self.click_on_element(HeaderPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step("Клик на Конструктор в хедере страницы")
    def click_on_constructor_button(self):
        self.click_on_element(HeaderPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик на Ленту заказов в хедере страницы")
    def click_on_order_feed_button(self):
        self.click_on_element(HeaderPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Проверяем переход в Конструктор бургера")
    def check_burger_constructor_page(self):
        return self.find_element_with_waiting(MainPageLocators.LABEL_BUILD_BURGER)

    @allure.step("Проверяем переход в Ленту заказов")
    def check_order_feed_page(self):
        return self.find_element_with_waiting(MainPageLocators.LABEL_ORDER_FEED)
