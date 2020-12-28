import pytest
from appium import webdriver

'''执行步骤：
1、打开雪球app，进入首页
2、点击搜索输入框
3、输入阿里巴巴
4、搜索结果选择"阿里巴巴"，点击
5、获取"香港 阿里巴巴"股票的股价，并判断股值>200
'''


class TestAndriod():
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

        # 键盘默认中文输入，所以输入中文，要重设输入法
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        print('获取的股价是:{0}'.format(current_price))
        assert current_price > 200


if __name__ == '__main__':
    pytest.main()
