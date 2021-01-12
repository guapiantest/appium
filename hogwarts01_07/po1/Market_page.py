from selenium.webdriver.common.by import By

from hogwarts01_07.base_page import BasePage
from hogwarts01_07.po1.search_page import SearchPage


class Market(BasePage):
    def goto_search(self):
        self.find_and_click(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/action_search"]')
        return SearchPage(self.driver)
