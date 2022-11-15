import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from pages.digest_auth import DigestAuth


class TestDigestAuth(unittest.TestCase):
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    def setUp(self) -> None:
        self.driver.get('https://the-internet.herokuapp.com')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_valid_credential_digest_auth(self):
        digest_auth = DigestAuth(self.driver)
        digest_auth.valid_credential_auth()