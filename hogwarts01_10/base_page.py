import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from hogwarts01_10.testcase2.black_handle import black_wrapper
"""
todo:封装自己的黑名单类
解决基类无限膨胀，设计模式：代理模式，装饰器模式
"""

class BasePage:
    def __init__(self):
        caps = {}
        caps["platformName"] = 'Android'
        caps["deviceName"] = 'emulator-5554'
        caps["appPackage"] = 'com.xueqiu.android'
        caps["appActivity"] = '.common.MainActivity'
        caps["noReset"] = 'true'  # 不初始化设备
        # caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    @black_wrapper
    def find(self, by, locator):
        # self.driver.save_screenshot('tmp.png')
        return self.driver.find_element(by, locator)

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

    def load(self, yaml_path):
        with open(yaml_path, encoding='utf-8') as f:
            data = yaml.load(f)
        for step in data:
            xpath_expr = step.get('element')
            action = step.get("action")
            if action == "find and click":
                self.find_and_click(By.XPATH, xpath_expr)
            elif action == "find and send":
                content = step.get("content")
                self.find_and_send(By.XPATH, xpath_expr, content)

    # 尝试将各个页面的yaml文件内容汇总到一个文件内
    def load2(self, yaml_path, page_yaml):
        with open(yaml_path, 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f).get(page_yaml)
            for step in data:
                xpath_expr = step['element']
                action = step["action"]
                if action == "find and click":
                    self.find_and_click(By.XPATH, xpath_expr)
                    print(page_yaml+"find_and_click执行成功")
                elif action == "find and send":
                    content = step["content"]
                    self.find_and_send(By.XPATH, xpath_expr, content)
                    print(page_yaml + "find_and_send执行成功")

    def screenshot(self,pic_path):
        self.driver.save_screenshot(pic_path)
