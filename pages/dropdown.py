"""
Dropdown
"""
import time
from pages.abase_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Dropdown(BasePage):
    DROPDOWN = (By.XPATH, '//*[@id="content"]/ul/li[11]/a')
    DROPDOWN_LIST = (By.ID, 'dropdown')
    OPTION1 = (By.CSS_SELECTOR, '#dropdown > option:nth-child(2)')
    OPTION2 = (By.CSS_SELECTOR, '#dropdown > option:nth-child(3)')

    def dropdown_opt1(self):
        self.driver.find_element(*Dropdown.DROPDOWN).click()
        self.driver.find_element(*Dropdown.DROPDOWN_LIST)
        self.driver.find_element(*Dropdown.OPTION1).click()
        time.sleep(3)

    def dropdown_opt2(self):
        self.driver.find_element(*Dropdown.DROPDOWN).click()
        self.driver.find_element(*Dropdown.DROPDOWN_LIST)
        self.driver.find_element(*Dropdown.OPTION2).click()
        time.sleep(3)

    def dropdown_with_select(self):
        self.driver.find_element(*Dropdown.DROPDOWN).click()
        dropdown = self.driver.find_element(*Dropdown.DROPDOWN_LIST)
        dd = Select(dropdown)
        dd.select_by_index(1) # index 0 is disable
        time.sleep(3)
        dd.select_by_visible_text("Option 2")
        time.sleep(3)
        dd.select_by_value("1")
        time.sleep(3)

    def dropdown_stress_opt(self):
        self.driver.find_element(*Dropdown.DROPDOWN).click()
        self.driver.find_element(*Dropdown.DROPDOWN_LIST)
        e = 0
        while e < 10:
            self.driver.find_element(*Dropdown.OPTION1).click()
            time.sleep(1)
            self.driver.find_element(*Dropdown.OPTION2).click()
            time.sleep(1)
            e += 1





