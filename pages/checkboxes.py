"""
Checkboxes
"""
import time

from pages.abase_page import BasePage
from selenium.webdriver.common.by import By


class Checkboxes(BasePage):
    CHECKBOX_PAGE = (By.CSS_SELECTOR, '#content > ul > li:nth-child(6) > a')
    CHECKBOX_1 = (By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)')
    CHECKBOX_2 = (By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)')

    def click_on_checkbox_1(self):
        self.driver.find_element(*Checkboxes.CHECKBOX_1).click()
        time.sleep(3)

    def click_on_checkbox_2(self):
        self.driver.find_element(*Checkboxes.CHECKBOX_PAGE).click()
        self.driver.find_element(*Checkboxes.CHECKBOX_2).click()

    def checkbox_true_or_false(self):
        self.driver.find_element(*Checkboxes.CHECKBOX_1).click()
        var1 = self.driver.find_element(*Checkboxes.CHECKBOX_1).is_selected()
        print(var1)
        time.sleep(3)
        self.driver.find_element(*Checkboxes.CHECKBOX_2).click()
        var2 = self.driver.find_element(*Checkboxes.CHECKBOX_2).is_selected()
        print(var2)
        time.sleep(3)
