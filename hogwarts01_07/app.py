from appium import webdriver
from hogwarts01_07.base_page import BasePage
from hogwarts01_07.po1.main import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = 'Android'
            caps["deviceName"] = 'emulator-5554'
            caps["appPackage"] = 'com.xueqiu.android'
            caps["appActivity"] = '.common.MainActivity'
            caps["noReset"] = 'true'  # 不初始化设备
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()

        return self

    def goto_main(self):
        return MainPage(self.driver)
