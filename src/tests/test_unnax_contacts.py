import unittest
from src.page_objects.contacts import ContactsPage
from src.common.chromedriver_obj import Driver


chromedriver_path = '/home/luis/Programs/chromedriver/chromedriver'


class TestUnnaxContactForm(unittest.TestCase):
    """A sample test class to show how page object works"""

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver(chromedriver_path)

    def setUp(self):
        self.driver.navigate("https://www.unnax.com/contact/")

    def test_submiting_contact_form(self):
        contacts_page = ContactsPage(self.driver.instance)
        contacts_page.fill_contact_form('test', 'test', 'seplusi@gmail.com', 'test', '012345678', 'test')
        assert(contacts_page.send_request() == "Thanks, we will be in touch shortly.")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()


if __name__ == "__main__":
    unittest.main()
