from selenium.webdriver.common.by import By


class RestorePasswordPageLocators:
    RESTORE_PASSWORD_LINK = [By.XPATH, ".//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']"]
    RESTORE_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button_size_medium') and text()='Восстановить']"]
    EMAIL_FIELD_FOR_RESTORE_PASSWORD = [By.CSS_SELECTOR, "input[type=text]"]
    SAVE_BUTTON = [By.XPATH, ".//button[contains(@class, 'button_button_size_medium') and text()='Сохранить']"]
    SHOW_HIDE_PASSWORD_BUTTON = [By.XPATH, ".//form//label[text()='Пароль']//following::*[local-name()='svg']"]
    PASSWORD_FIELD_WHEN_ACTIVE = [By.XPATH, ".//div[contains(@class, 'input_status_active')]"]
