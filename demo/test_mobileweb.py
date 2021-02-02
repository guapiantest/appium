from time import sleep

from appium import webdriver


class TestBrowser:
    def setup(self):
        caps ={}
        caps["platformName"] = 'android'
        caps["deviceName"] = 'emulator-5554'
        # caps["noReset"] = True
        caps["browserName"] = 'Browser'  # 使用自带浏览器
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://www.baidu.com")
        sleep(2)