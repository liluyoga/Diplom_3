from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    EMAIL_FIELD_INPUT = [By.CSS_SELECTOR, "input[type=text]"]
    PASSWORD_FIELD_INPUT = [By.CSS_SELECTOR, "input[type=password]"]
    LOGIN_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button_size_medium') and text()='Войти']"]
    PROFILE_LIST_LOGIN = [By.XPATH, ".//label[text()='Логин']/parent::div/input[@value]"]
    ORDER_HISTORY_BUTTON = [By.XPATH, ".//a[@href='/account/order-history']"]
    EXIT_BUTTON = [By.XPATH, ".//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']"]
