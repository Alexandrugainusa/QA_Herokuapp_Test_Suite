"""
Dynamic Controls
"""
import time

from pages.abase_page import BasePage
from selenium.webdriver.common.by import By


class DynamicControls(BasePage):
    ADD_REMOVE_BTN = (By.XPATH, '//*[@id="checkbox-example"]/button')
    A_CHECKBOX = (By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
    ENABLE_DISABLE_BTN = (By.XPATH, '//*[@id="input-example"]/button')

    def wait_for_load_icon_finish(self):
        self.driver.find_element(*DynamicControls.A_CHECKBOX).click()
        time.sleep(3)
        self.driver.find_element(*DynamicControls.ADD_REMOVE_BTN).click()
        time.sleep(3)
        # self.driver.find_element(*DynamicControls.A_CHECKBOX).click()
        # time.sleep(3)
