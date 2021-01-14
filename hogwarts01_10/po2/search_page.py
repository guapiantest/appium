import yaml
from selenium.webdriver.common.by import By
from hogwarts01_10.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        # self.load('../po2/search_page.yaml')
        self.load2('../po2/big.yaml', 'searchyaml')
        return True
