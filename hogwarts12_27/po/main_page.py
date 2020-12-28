from appium.webdriver.common.mobileby import MobileBy
from hogwarts12_27.po.address_list_page import AddressListPage
from hogwarts12_27.po.base_page import BasePage


class MainPage(BasePage):
    """首页po"""

    def goto_addresslist(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
