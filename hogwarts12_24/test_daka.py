import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDaka:

    def setup(self):
        caps = {}
        caps["platformName"] = 'Android'
        caps["deviceName"] = 'emulator-5554'
        caps["appPackage"] = 'com.tencent.wework'
        caps["appActivity"] = '.launch.WwMainActivity'
        # 这一步很关键,否则打开的企业微信需要重新登录
        caps["noReset"] = 'true'
        # 修改页面的空闲状态的时间为0，加快打卡页面的渲染速度
        caps['settings[waitForIdleTimeout]'] = 0

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)  #隐式等待只针对find元素生效

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        #直到底部菜单出现"我",再去找"工作台"，否则触发显式等待6秒
        WebDriverWait(self.driver,6).until(lambda diver:self.driver.find_element_by_xpath("//*[@text='我']"))
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        # 滑动页面，找到打卡按钮
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]").click() #点击包含次打开的元素
        print(self.driver.page_source)

        '''判断页面出现"外出打卡成功"才执行下一步，否则触发显示等待12秒再进行下一步'''
        WebDriverWait(self.driver,12).until(lambda x:"外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source
