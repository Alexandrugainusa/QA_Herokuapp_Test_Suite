import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.broken_images import BrokenImages


class TestBrokenImages(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        self.driver.get('https://the-internet.herokuapp.com/')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_url(self): # THIS TEST SHOULD FAIL
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/broken_images'
        self.assertEqual(expected, actual, 'URL is incorrect')

    def test_broken_images(self):
        broken_img = BrokenImages(self.driver)
        broken_img.broken_img()

    def test_valid_or_broken_img(self):
        images = BrokenImages(self.driver)
        images.check_broken_img_status_code()


