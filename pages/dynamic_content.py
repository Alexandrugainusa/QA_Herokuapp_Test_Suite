"""
Dynamic Content
"""
from pages.abase_page import BasePage
from selenium.webdriver.common.by import By


class DynamicContent(BasePage):
    CONTENT_PAGE = (By.TAG_NAME, 'row')

    def get_content(self):
        review = self.driver.find_elements(*DynamicContent.CONTENT_PAGE)
        for post in review:
            content = post.find_element(By.XPATH, '//*[@id="content"]/div[1]').text
            # print(post.text)
            print(content)



