from appium.webdriver.common.mobileby import MobileBy
from hogwarts12_27.po.base_page import BasePage


class AddressListPage(BasePage):
    def click_addmember(self):
        from hogwarts12_27.po.member_invite_menu_page import MemberInviteMenuPage

        self.scroll_find("添加成员")
        return MemberInviteMenuPage(self.driver)

    def get_memberlist(self):
        '''没找到元素，此处待修改'''
        lists = self.find(MobileBy.XPATH, "//*[@class='android.widget.TextView']")
        print(lists)
        member_list_res = [i.text for i in lists]
        return member_list_res
