import allure

from data import TestData
from locators.header_page_locators import HeaderPageLocators
from locators.restore_password_page_locators import RestorePasswordPageLocators
from pages.base_page import BasePage


class RestorePasswordPage(BasePage):

    @allure.step("Кликаем на Личный кабинет и затем на ссылку Восстановить пароль")
    def click_on_restore_password_link_from_personal_account(self):
        self.click_on_element(HeaderPageLocators.PERSONAL_ACCOUNT_LINK)
        self.click_on_element(RestorePasswordPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step("Вводим почту в поле Email и кликаем по кнопке Восстановить")
    def input_email_and_click_on_button_restore(self):
        self.click_on_restore_password_link_from_personal_account()
        self.input_value_to_field(RestorePasswordPageLocators.EMAIL_FIELD_FOR_RESTORE_PASSWORD, TestData.USER_EMAIL)
        self.click_on_element(RestorePasswordPageLocators.RESTORE_BUTTON)

    @allure.step("Проверяем наличие кнопки Сохранить на странице")
    def check_button_save_on_page(self):
        return self.find_element_with_waiting(RestorePasswordPageLocators.SAVE_BUTTON)

    @allure.step("Кликаем на кнопку показать/скрыть пароль")
    def click_on_visible_password_eye(self):
        self.click_on_restore_password_link_from_personal_account()
        self.input_email_and_click_on_button_restore()
        self.click_on_element(RestorePasswordPageLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step("Проверка, что поле стало активным")
    def check_field_is_active(self):
        return self.find_element_with_waiting(RestorePasswordPageLocators.PASSWORD_FIELD_WHEN_ACTIVE)
