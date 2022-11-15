import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.disappering_elements import DisapperingElements


class TestDisapperingElements(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        self.driver.get('https://the-internet.herokuapp.com/disappearing_elements')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_disappering_elem(self):
        gallery_disappering_elem = DisapperingElements(self.driver)
        gallery_disappering_elem.disappering_elem()