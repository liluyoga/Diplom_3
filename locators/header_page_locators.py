from selenium.webdriver.common.by import By


class HeaderPageLocators:
    PERSONAL_ACCOUNT_LINK = [By.XPATH,
                             ".//p[contains(@class, 'AppHeader_header__linkText') and text()='Личный Кабинет']"]
    CONSTRUCTOR_BUTTON = [By.XPATH, ".//p[contains(@class, 'AppHeader_header__linkText') and text()='Конструктор']"]
    ORDER_FEED_BUTTON = [By.XPATH, ".//p[contains(@class, 'AppHeader_header__linkText') and text()='Лента Заказов']"]
