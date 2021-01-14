from hogwarts01_10.po2.pre_page import PrePage
from hogwarts01_10.po2.search_page import SearchPage


class Market(PrePage):
    def goto_search(self):
        # self.load('../po2/Market_page.yaml')

        self.basepage.load2('../po2/big.yaml','marketyaml')
        return SearchPage(self.basepage)
