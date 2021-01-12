from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from hogwarts01_07.base_page import BasePage
from hogwarts01_07.po1.Market_page import Market


class MainPage(BasePage):
    def goto_market(self):
        self.find_and_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']") # 模拟弹窗
        self.find_and_click(By.XPATH,"//*[@resource-id='android:id/tabhost']//*[@text='行情']")
        return Market(self.driver)