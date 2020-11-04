from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.common.test_common import TestCommon


class ContactsPage(TestCommon):
    """
        Page object that represents the page with the conversion result
    """

    CONTACT_FORM = "section.has_ae_slider.ob-is-breaking-bad[data-settings*='{\"backgr']"
    FIRSTNAME_TEXT_BOX = "input.hs-input[name=\"firstname\"]"
    LASTNAME_TEXT_BOX = "input.hs-input[name=\"lastname\"]"

    def __init__(self, driver):
        super(ContactsPage, self).__init__(driver)
        self.driver = driver
        self.wait_for_element(By.CSS_SELECTOR, self.CONTACT_FORM)

        self.contact_form = self.driver.find_element_by_css_selector(self.CONTACT_FORM)
        self.name_text_box = self.contact_form.find_element_by_css_selector(self.FIRSTNAME_TEXT_BOX)
        self.surname_text_box = self.contact_form.find_element_by_css_selector(self.LASTNAME_TEXT_BOX)
        print("fghjk")
