import allure

from pages.header_page import HeaderPage


class TestHeaderPage:

    @allure.title("Переход по клику на Конструктор")
    def test_crossing_burger_constructor(self, driver):
        page = HeaderPage(driver)
        page.click_on_constructor_button()
        result = page.check_burger_constructor_page

        assert result

    @allure.title("Переход по клику на Лента заказов")
    def test_crossing_order_feed(self, driver):
        page = HeaderPage(driver)
        page.click_on_order_feed_button()
        result = page.check_order_feed_page

        assert result
