import unittest
import time
from src.page_objects.contacts import ContactsPage
from src.common.chromedriver_obj import Driver


chromedriver_path = '/home/luis/Programs/chromedriver/chromedriver'


class TestCurrencyConverter(unittest.TestCase):
    """A sample test class to show how page object works"""

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver(chromedriver_path)

    def setUp(self):
        self.driver.navigate("https://www.unnax.com/contact/")

    def test1(self):
        ContactsPage(self.driver.instance)
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()


if __name__ == "__main__":
    unittest.main()
