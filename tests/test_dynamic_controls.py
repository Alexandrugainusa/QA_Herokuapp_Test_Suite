import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.dynamic_controls import DynamicControls


class TestDynamicControls(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        self.driver.get('https://the-internet.herokuapp.com/dynamic_controls')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_wait_finish_loading(self):
        loading = DynamicControls(self.driver)
        loading.wait_for_load_icon_finish()