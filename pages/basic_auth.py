"""
Authentication
"""
import time

from selenium.webdriver.common.by import By

from pages.abase_page import BasePage


class BasicAuth(BasePage):
    PROMPT_MENU = (By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a')
    VALID_USER = 'admin'
    VALID_PASS = 'admin'

    def valid_credential(self):
        self.driver.find_element(*BasicAuth.PROMPT_MENU).click()
        self.driver.get(
            'https://' + self.VALID_USER + ':' + self.VALID_PASS + '@the-internet.herokuapp.com/basic_auth'
        )
        time.sleep(3)
