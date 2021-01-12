from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from hogwarts01_07.testcase1.black_handle import black_wrapper

"""
todo:封装自己的黑名单类
解决基类无限膨胀，设计模式：代理模式，装饰器模式
"""


class BasePage:
    """接收driver，这样每继承一次基类，就会把上一页面的driver接收过来"""
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        # 黑名单列表
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    # 整体思路：捕获元素没找到的异常，然后去黑名单中去找能使弹窗关闭的元素，若找到，则进行点击，可以处理掉当前弹窗
    # 相当于把能使弹窗关闭的元素放到黑名单

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)
        # try:
        #     return self.driver.find_element(by, locator)
        # # 捕获元素没找到的异常
        # except Exception as e:
        #     # 遍历黑名单中的所有元素，去进行查找
        #     for black in self.black_list:
        #         eles = self.finds(*black)  # 元素订单，可能会查到多个，所以是finds,列表
        #         if len(eles) > 0:
        #             # 对很名单元素进行点击
        #             eles[0].click()
        #             return self.find(by, locator)  # 递归函数，处理好之后，返回自己
        #     raise e  # 黑名单元素也没找到，抛出异常

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def scroll_find(self, text):
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      f'text("{text}").instance(0));').click()

    def find_and_click(self, by, locator):
        return self.find(by, locator).click()

    def find_and_send(self, by, locator, value):
        return self.find(by, locator).send_keys(value)
