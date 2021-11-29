from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).click()

    def get_title(self, title):
        WebDriverWait(self.driver, 5).until(EC.title_is(title))
        return self.driver.title

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).send_keys(text, Keys.RETURN)


