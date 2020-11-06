from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_find_element(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))
