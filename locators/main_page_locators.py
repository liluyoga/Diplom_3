from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_LINK = [By.XPATH,
                             ".//p[contains(@class, 'AppHeader_header__linkText') and text()='Личный Кабинет']"]
    CONSTRUCTOR_BUTTON = [By.XPATH, ".//p[contains(@class, 'AppHeader_header__linkText') and text()='Конструктор']"]
    ORDER_FEED_BUTTON = [By.XPATH, ".//p[contains(@class, 'AppHeader_header__linkText') and text()='Лента Заказов']"]

    BUTTON_PLACE_ORDER = [By.XPATH,
                          ".//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']"]
    LABEL_BUILD_BURGER = [By.XPATH, ".//h1[text()='Соберите бургер']"]
    LABEL_ORDER_FEED = [By.XPATH, ".//h1[text()='Лента заказов']"]
    LABEL_INGREDIENT_DETAILS = [By.XPATH,
                                ".//section[contains(@class, 'Modal_modal_opened')]//h2[text()='Детали ингредиента']"]
    INGREDIENT = [By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]"]
    CLOSE_INGREDIENT_DETAILS = [By.XPATH,
                                ".//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close_modified')]"]
    MODAL_OPENED = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]"]
    INGREDIENT_COUNTER = [By.XPATH,
                          ".//a[contains(@class, 'BurgerIngredient_ingredient_')]//p[contains(@class, 'counter_counter__num')]"]
    BURGER_BASKET = [By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"]
    ORDER_PLACED = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p[text()='идентификатор заказа']"]
    ORDER_NUMBER = [By.XPATH, ".//div[contains(@class, 'Modal_modal__contentBox')]/h2"]
    CLOSE_ORDER_MODAL_WINDOW = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified')]"]
