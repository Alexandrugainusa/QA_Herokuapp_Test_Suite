"""
Digest Authentication
"""
import time

from pages.abase_page import BasePage
from selenium.webdriver.common.by import By


class DigestAuth(BasePage):
    PROMPT_MENU = (By.CSS_SELECTOR, '#content > ul > li:nth-child(8) > a')
    VALID_USER_AUTH = 'admin'
    VALID_PASS_AUTH = 'admin'

    def valid_credential_auth(self):
        self.driver.find_element(*DigestAuth.PROMPT_MENU).click()
        self.driver.get(
            'https://' +
            self.VALID_USER_AUTH + ':' +
            self.VALID_PASS_AUTH + '@the-internet.herokuapp.com/digest_auth'
        )
        time.sleep(3)
