from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER = [By.XPATH, ".//a[contains(@class, 'OrderHistory_link')]"]
    ORDER_DETAILS = [By.XPATH,
                     ".//section[contains(@class, 'Modal_modal_opened')]//ul/li/div[contains(@class, 'Modal_imgBox')]"]
    ORDERS_IN_HISTORY_AND_ORDER_FEED = [By.XPATH,
                                        ".//div[contains(@class, 'OrderHistory_textBox')]/p[@class='text text_type_digits-default']"]
    COMPLETED_ORDERS_ALL_TIME_BEFORE = [By.XPATH, ".//div/p[text()='Выполнено за все время:']/following-sibling::p"]
    COMPLETED_ORDERS_ALL_TIME_FOR_FIND = [By.XPATH,
                                          ".//div/p[text()='Выполнено за все время:']/following-sibling::p[text()='{}']"]
    COMPLETED_ORDERS_TODAY_BEFORE = [By.XPATH, ".//div/p[text()='Выполнено за сегодня:']/following-sibling::p"]
    COMPLETED_ORDERS_TODAY_FOR_FIND = [By.XPATH,
                                       ".//div/p[text()='Выполнено за сегодня:']/following-sibling::p[text()='{}']"]
    ORDERS_IN_PROGRESS = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li"]
    LABEL_ALL_ORDERS_ARE_READY = [By.XPATH,
                                  ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='Все текущие заказы готовы!']"]
    ORDER_LIST = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='{}']"]
