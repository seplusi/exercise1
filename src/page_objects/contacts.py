from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.common.test_common import TestCommon


class ContactsPage(TestCommon):
    """
        Page object that represents the page with the conversion result
    """

    CONTACT_FORM = "section.has_ae_slider.ob-is-breaking-bad[data-settings*='{\"backgr']"
    LIST_CONTACT_FORM_SELECTOR = ['firstname', 'lastname', 'email', 'company', 'phone', 'message']
    SEND_REQUEST_BUTTON = "input.hs-button.primary.large"
    AGREEMENT_BOX = "input.hs-input[name='lopd']"
    SUBMITED_MSG = "div.submitted-message.hs-main-font-element"
    FIRSTNAME_TEXT_BOX = "input.hs-input[name='firstname']"
    LASTNAME_TEXT_BOX = "input.hs-input[name='lastname']"
    EMAIL_TEXT_BOX = "input.hs-input[name='email']"
    COMPANY_TEXT_BOX = "input.hs-input[name='company']"
    PHONE_TEXT_BOX = "input.hs-input[name='phone']"
    MESSAGE_TEXT_BOX = "input.hs-input[name='message']"

    def __init__(self, driver):
        super(ContactsPage, self).__init__(driver)
        self.driver = driver
        self.wait_for_element(By.CSS_SELECTOR, self.CONTACT_FORM)

        self.contact_form = self.driver.find_element_by_css_selector(self.CONTACT_FORM)
        self.name_text_box = self.contact_form.find_element_by_css_selector(self.FIRSTNAME_TEXT_BOX)
        self.surname_text_box = self.contact_form.find_element_by_css_selector(self.LASTNAME_TEXT_BOX)
        self.email_text_box = self.contact_form.find_element_by_css_selector(self.EMAIL_TEXT_BOX)
        self.company_text_box = self.contact_form.find_element_by_css_selector(self.COMPANY_TEXT_BOX)
        self.phone_text_box = self.contact_form.find_element_by_css_selector(self.PHONE_TEXT_BOX)
        
    def send_request(self, *args):
        for index in range(0, len(self.LIST_CONTACT_FORM_SELECTOR)):
            self.contact_form.find_element_by_css_selector(self.LIST_CONTACT_FORM_SELECTOR[index]).send_keys(args[index])
        
        self.contact_form.find_element_by_css_selector(self.AGREEMENT_BOX).click()
        self.contact_form.find_element_by_css_selector(self.SEND_REQUEST_BUTTON).click()
        
        self.self.wait_for_element(By.CSS_SELECTOR, self.SUBMITED_MSG)
        
        return self.driver.find_element_by_css_selector(self.AGREEMENT_BOX).text
