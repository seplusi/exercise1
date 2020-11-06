from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCommon:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by_locator)))

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
