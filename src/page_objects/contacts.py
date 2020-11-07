from src.common.base_page import BasePage
from src.common.locators import Locators


class ContactsPage(BasePage):
    """
        Page object that represents the contacts page
    """

    def __init__(self, driver, *args):
        super(ContactsPage, self).__init__(driver)
        self.driver = driver
        self.contact_form = self.wait_find_element(Locators.CONTACT_FORM)

    def fill_contact_form(self, *args):
        """
            Fills the contact form

        :param args: List of Strings to be written in the contact form
        :return: None
        """
        self.contact_form.find_element(*Locators.FIRSTNAME_TEXT_BOX).send_keys(args[0])
        self.contact_form.find_element(*Locators.LASTNAME_TEXT_BOX).send_keys(args[1])
        self.contact_form.find_element(*Locators.EMAIL_TEXT_BOX).send_keys(args[2])
        self.contact_form.find_element(*Locators.COMPANY_TEXT_BOX).send_keys(args[3])
        self.contact_form.find_element(*Locators.PHONE_TEXT_BOX).send_keys(args[4])
        self.contact_form.find_element(*Locators.MESSAGE_TEXT_BOX).send_keys(args[5])

    def send_request(self):
        """
            Accepts the terms & conditions and submits the request form

        :return: None
        """
        self.contact_form.find_element(*Locators.AGREEMENT_BOX).click()
        self.contact_form.find_element(*Locators.SEND_REQUEST_BUTTON).click()

        return self.wait_find_element(Locators.SUBMITED_MSG).text
