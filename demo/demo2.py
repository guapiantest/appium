import pytest
from appium import webdriver


class TestUiauto():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        '''以下三步，是为了处理首页弹窗'''
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    def test_getvalue(self):
        # 查找首页搜索框元素
        element = self.driver.find_element_by_id('com.xueqiu.android:id/home_search')
        print(element.text)
        print(element.location)  # 打印坐标
        print(element.size)  # 打印高度、宽度
        # 判断找到的元素是否可见
        if element.is_enabled() == True:
            element.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")  # 搜索结果第一个元素
            if alibaba_element.get_attribute("enabled") == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        # 实例化TouchAction,需要传入参数driver
        from appium.webdriver.common.touch_action import TouchAction
        action = TouchAction(self.driver)
        action.press(x=731, y=2083).wait(200).move_to(x=731, y=484).perform()


if __name__ == '__main__':
    pytest.main()
