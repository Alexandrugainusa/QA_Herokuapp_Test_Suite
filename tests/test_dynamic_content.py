import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.dynamic_content import DynamicContent


class TestDynamicContent(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        self.driver.get('https://the-internet.herokuapp.com/dynamic_content?with_content=static')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_get_content_page(self):
        content_page = DynamicContent(self.driver)
        content_page.get_content()
