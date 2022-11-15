"""
Broken Images
"""
import time

import requests

from pages.abase_page import BasePage
from selenium.webdriver.common.by import By


class BrokenImages(BasePage):
    BROKEN_IMG = (By.CSS_SELECTOR, '#content > ul > li:nth-child(4) > a')
    IMG1 = (By.CSS_SELECTOR, '#content > div > img:nth-child(2)')
    IMG2 = (By.CSS_SELECTOR, '#content > div > img:nth-child(3)')
    IMG3 = (By.CSS_SELECTOR, '#content > div > img:nth-child(4)')

    def broken_img(self):
        self.driver.find_element(*self.BROKEN_IMG).click()
        time.sleep(3)

    def check_broken_img_status_code(self):
        self.driver.find_element(*self.BROKEN_IMG).click()
        first_img = self.driver.find_element(*self.IMG1)
        second_img = self.driver.find_element(*self.IMG2)
        third_img = self.driver.find_element(*self.IMG3)
        images_list = [first_img, second_img, third_img]

        for image in images_list:
            if requests.head(image.get_attribute("src")).status_code == 200:
                print("Valid image")
            else:
                print("Broken image")
        time.sleep(3)
