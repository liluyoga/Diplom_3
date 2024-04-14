import allure

from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step("Авторизация в личном кабинете")
    def personal_account_login(self, email, password):
        self.click_on_element(HeaderPageLocators.PERSONAL_ACCOUNT_LINK)
        self.input_value_to_field(PersonalAccountPageLocators.EMAIL_FIELD_INPUT, email)
        self.input_value_to_field(PersonalAccountPageLocators.PASSWORD_FIELD_INPUT, password)
        self.click_on_element(PersonalAccountPageLocators.LOGIN_BUTTON)
        self.find_element_with_waiting(MainPageLocators.BUTTON_PLACE_ORDER)

    @allure.step("Переход в Личный Кабинет")
    def go_to_personal_account(self):
        self.click_on_element(HeaderPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step("Забираем значение из поля Логин в Личном Кабинете")
    def get_login_field_value(self):
        element = self.find_element_with_waiting(PersonalAccountPageLocators.PROFILE_LIST_LOGIN).get_attribute('value')
        return element

    @allure.step("Переход в Историю заказов")
    def go_to_order_history(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Кликаем на Выход")
    def click_on_exit_button(self):
        self.click_on_element(PersonalAccountPageLocators.EXIT_BUTTON)
        return self.find_element_with_waiting(PersonalAccountPageLocators.LOGIN_BUTTON)
