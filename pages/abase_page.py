"""
Base Page
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
