import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.context_menu import ContextMenu


class TestContextMenu(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        self.driver.get('https://the-internet.herokuapp.com/context_menu')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_context_menu_right_click(self):
        context_menu = ContextMenu(self.driver)
        context_menu.context_menu_alert()