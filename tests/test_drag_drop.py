import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pages.drag_drop import DragDrop


class TestDragDrop(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        self.driver.get('https://the-internet.herokuapp.com/drag_and_drop')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_drag_drop(self):
        drag_drop = DragDrop(self.driver)
        drag_drop.drag_drop()
