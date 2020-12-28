from appium import webdriver

from hogwarts12_27.po.base_page import BasePage
from hogwarts12_27.po.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = 'Android'
            caps["deviceName"] = 'emulator-5554'
            caps["appPackage"] = 'com.tencent.wework'
            caps["appActivity"] = '.launch.WwMainActivity'
            caps["noReset"] = 'true'
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()

        return self

    def goto_main(self):
        return MainPage(self.driver)
