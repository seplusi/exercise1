from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCommon:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by_locator, selector, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by_locator, selector)))
        return self.driver.find_element(by_locator, selector)
