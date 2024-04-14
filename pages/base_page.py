from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_waiting(self, locator, time=15):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_all_elements_with_waiting(self, locator, time=15):
        WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator, time=30):
        click = ActionChains(self.driver)
        element = self.find_element_with_waiting(locator, time)
        click.move_to_element(element).click().perform()

    def input_value_to_field(self, locator, value):
        element = self.find_element_with_waiting(locator)
        element.send_keys(value)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url


    def drag_and_drop(self, locator_1, locator_2):
        ingredient = self.find_element_with_waiting(locator_1)
        basket = self.find_element_with_waiting(locator_2)
        ActionChains(self.driver).drag_and_drop(ingredient, basket).perform()

    def get_text_from_element(self, locator):
        return self.find_element_with_waiting(locator).text

    def wait_until_invisibility_element(self, locator):
        WebDriverWait(self.driver, 25).until(EC.invisibility_of_element_located(locator))

    def wait_until_not_text_to_be_present(self, locator, text):
        WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(locator, text))

    @staticmethod
    def concat_locator_and_number(locator, value):
        method, locator = locator
        return method, locator.format(value)
