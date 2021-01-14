from hogwarts01_10.po2.pre_page import PrePage


class SearchPage(PrePage):
    def search(self):
        # self.load('../po2/search_page.yaml')
        self.basepage.load2('../po2/big.yaml', 'searchyaml')
        return True
