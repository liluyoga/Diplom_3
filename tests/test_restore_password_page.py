import allure

from data import TestData
from pages.restore_password_page import RestorePasswordPage


class TestLoginPage:

    @allure.title("Переход на страницу восстановления пароля по кнопке Восстановить пароль")
    def test_crossing_to_forgot_password_page(self, driver):
        page = RestorePasswordPage(driver)
        page.click_on_restore_password_link_from_personal_account()
        actual_result = page.get_current_url()

        assert TestData.URL_FORGOT_PASSWORD in actual_result

    @allure.title("Ввод Email и и клик по кнопке Восстановить")
    def test_crossing_to_reset_password_page(self, driver):
        page = RestorePasswordPage(driver)
        page.input_email_and_click_on_button_restore()
        result = page.check_button_save_on_page()

        assert result

    @allure.title("Клик по кнопке показать/скрыть пароль подсвечивает поле")
    def test_password_field_active(self, driver):
        page = RestorePasswordPage(driver)
        page.click_on_visible_password_eye()
        result = page.check_field_is_active()

        assert result
