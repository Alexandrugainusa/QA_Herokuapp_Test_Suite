"""
Context Menu
"""
import time

from selenium.webdriver import ActionChains

from pages.abase_page import BasePage
from selenium.webdriver.common.by import By


class ContextMenu(BasePage):
    CONTEXT_MENU = (By.CSS_SELECTOR, '#hot-spot')
    RIGHT_CLICK = (By.ID, 'hot-spot')

    def context_menu_alert(self):
        self.driver.find_element(*ContextMenu.CONTEXT_MENU).click()
        action = ActionChains(self.driver)  # ii trimitem driveru de Chrome
        action.context_click(self.driver.find_element(*ContextMenu.RIGHT_CLICK)).perform()
        self.driver.switch_to.alert.accept()  # accepta Alerta
        time.sleep(3)
