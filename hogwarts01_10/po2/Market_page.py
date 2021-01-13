import yaml
from selenium.webdriver.common.by import By

from hogwarts01_10.base_page import BasePage
from hogwarts01_10.po2.search_page import SearchPage


class Market(BasePage):
    def goto_search(self):
        # self.load('../po2/Market_page.yaml')

        self.load2('../po2/big.yaml','marketyaml')
        return SearchPage(self.driver)
