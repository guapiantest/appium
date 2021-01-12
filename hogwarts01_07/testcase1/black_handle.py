from selenium.webdriver.common import by

#封装黑名单装饰器

def black_wrapper(fuction):  #fuction参数是被装饰的方法
    def base_fun(*args, **kwargs):
        # 装饰器特性，传入的第0个参数为self
        self = args[0]  # 不太理解？
        try:
            return fuction(*args, **kwargs)
        except Exception as e:
            # 遍历黑名单中的所有元素，去进行查找,找到点击，找不到，抛出异常
            for black in self.black_list:
                eles = self.finds(*black)  # 元素订单，可能会查到多个，所以是finds,列表
                if len(eles) > 0:
                    # 对黑名单元素进行点击
                    eles[0].click()
                    return fuction(*args, **kwargs)  # 递归函数，处理好之后，返回自己
            raise e
    return base_fun
