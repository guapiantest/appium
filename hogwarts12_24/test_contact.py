import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class TestDaka:

    def setup(self):
        caps = {}
        caps["platformName"] = 'Android'
        caps["deviceName"] = 'emulator-5554'
        caps["appPackage"] = 'com.tencent.wework'
        caps["appActivity"] = '.launch.WwMainActivity'
        caps["noReset"] = 'true'
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        # self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        # 成员列表页面，若列表超出一屏，需要滑动页面查找'添加成员'元素
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys('飞雪')
        self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@text='男']").click()

        # 等弹窗里的"女"元素出现，再进行点击
        def wait_ele_for(driver: WebDriver):
            ele = driver.find_elements_by_xpath("//*[@text='女']")
            return len(ele) > 0
        WebDriverWait(self.driver, 10).until(wait_ele_for)
        self.driver.find_element_by_xpath("//*[@text='女']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys('15921057777')
        self.driver.find_element_by_xpath("//*[@text='保存']").click()

