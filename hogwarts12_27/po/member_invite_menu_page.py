from appium.webdriver.common.mobileby import MobileBy
from hogwarts12_27.po.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    def add_member_manual(self):
        from hogwarts12_27.po.contact_add_page import ContactAddPage

        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAddPage(self.driver)
