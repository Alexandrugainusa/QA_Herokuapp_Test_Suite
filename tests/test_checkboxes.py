import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.checkboxes import Checkboxes


class TestCheckboxes(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        self.driver.get('https://the-internet.herokuapp.com/checkboxes')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_url(self):
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/checkboxes'
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_click_checkbox1(self):
        checkbox = Checkboxes(self.driver)
        checkbox.click_on_checkbox_1()

    def test_click_checkbox2(self):  # THIS TEST SHOULD FAIL
        checkbox = Checkboxes(self.driver)
        checkbox.click_on_checkbox_2()

    def test_checkbox_true_or_false(self):
        checkbox = Checkboxes(self.driver)
        checkbox.checkbox_true_or_false()
