"""
Drag and Drop
"""
import time
import pyautogui

from selenium.webdriver import ActionChains

from pages.abase_page import BasePage
from selenium.webdriver.common.by import By


class DragDrop(BasePage):
    DRAG_AND_DROP_MENU = (By.CSS_SELECTOR, '#content > ul > li:nth-child(10) > a')
    OBJECT_A = (By.XPATH, '//*[@id="column-a"]')
    OBJECT_B = (By.XPATH, '//*[@id="column-b"]')

    def drag_drop(self):
        # self.driver.find_element(*DragDrop.DRAG_AND_DROP_MENU).click()  # click pe meniul drag and drop
        # action = ActionChains(self.driver)  # trimitem driveru de chrome
        # action.drag_and_drop(*DragDrop.OBJECT_A, *DragDrop.OBJECT_B).perform()
        pyautogui.moveTo(545, 228)
        pyautogui.dragTo(750, 230, duration=5)
        time.sleep(3)
