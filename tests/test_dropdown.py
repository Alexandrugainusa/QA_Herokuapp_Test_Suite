import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.dropdown import Dropdown


class TestDropdown(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        self.driver.get('https://the-internet.herokuapp.com/')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_dropdown_opt1(self):
        drop_menu = Dropdown(self.driver)
        drop_menu.dropdown_opt1()

    def test_dropdown_opt2(self):
        drop_menu = Dropdown(self.driver)
        drop_menu.dropdown_opt2()

    def test_dropdown_multi_opt(self):
        drop_menu = Dropdown(self.driver)
        drop_menu.dropdown_stress_opt()

    def test_dropdown_with_select(self):
        drop_menu = Dropdown(self.driver)
        drop_menu.dropdown_with_select()
