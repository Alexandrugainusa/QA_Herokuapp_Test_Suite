import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.basic_auth import BasicAuth


class TestBasicAuth(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_basic_auth(self):
        basic_auth = BasicAuth(self.driver)
        basic_auth.valid_credential()
