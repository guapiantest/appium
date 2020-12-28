from appium.webdriver.common.mobileby import MobileBy
from hogwarts12_27.po.base_page import BasePage


class ContactAddPage(BasePage):
    def add_contact(self):
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']", '飞雪')
        self.find_and_click(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']")
        # 等弹窗里的"女"元素出现，再进行点击
        # def wait_ele_for(driver: WebDriver):
        #     ele = driver.find_element(MobileBy.XPATH, "//*[@text='女']")
        #     # ele =self.find(MobileBy.XPATH,"//*[@text='女']")
        #     return len(ele) > 0

        # WebDriverWait(self.driver, 10).until(wait_ele_for)
        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']", '15921057777')
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

        return "成功添加用户"
