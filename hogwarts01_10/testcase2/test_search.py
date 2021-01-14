from hogwarts01_10.base_page import BasePage
from hogwarts01_10.po2.main import MainPage

class TestSearch:
    def setup(self):
        basepage = BasePage()
        self.app = MainPage(basepage)

    def test_search(self):
        self.app.goto_market().goto_search().search()
