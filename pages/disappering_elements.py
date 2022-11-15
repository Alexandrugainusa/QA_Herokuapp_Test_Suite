"""
Disappering Elements
"""
import time

from selenium.common import NoSuchElementException

from pages.abase_page import BasePage
from selenium.webdriver.common.by import By


class DisapperingElements(BasePage):
    GALLERY_DISAPPERING_ELEMENT = (By.XPATH, '//*[@id="content"]/div/ul/li[5]/a')
    PORTOFOLIO_BUTTON = (By.XPATH, '//*[@id="content"]/div/ul/li[4]/a')

    def disappering_elem(self):
        try:
            elem = self.driver.find_element(*DisapperingElements.GALLERY_DISAPPERING_ELEMENT).is_displayed()
            print(elem, '-> The element is displayed')
            time.sleep(3)
        except NoSuchElementException:
            print(False, "-> The element isn't displayed")
