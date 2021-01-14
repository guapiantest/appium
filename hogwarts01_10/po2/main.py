from hogwarts01_10.po2.Market_page import Market
from hogwarts01_10.po2.pre_page import PrePage


class MainPage(PrePage):
    def goto_market(self):
        # self.find_and_click(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']") # 模拟弹窗
        # self.find_and_click(By.XPATH,"//*[@resource-id='android:id/tabhost']//*[@text='行情']")

        # self.load("../po2/main.yaml")
        self.basepage.load2("../po2/big.yaml",'mainyaml')
        return Market(self.basepage)
