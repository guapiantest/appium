import logging

import allure

#封装黑名单装饰器
logging.basicConfig(level=logging.INFO)

def black_wrapper(fuction):  #fuction参数是被装饰的方法
    def base_fun(*args, **kwargs):
        # 装饰器特性，传入的第0个参数为self
        self = args[0]  # 不太理解？
        try:
            #查找元素时，进行日志打印
            logging.info('start find:'+str(args)+'kwargs:'+str(kwargs))
            return fuction(*args, **kwargs)
        except Exception as e:
            # 查不到元素时，进行截图，并存储在allure结果中
            self.screenshot('tmp.png')  # 调用截图方法
            with open('./tmp.png','rb') as f:
                picture_data = f.read()
            allure.attach(picture_data,attachment_type=allure.attachment_type.PNG)
            # 遍历黑名单中的所有元素，去进行查找,找到点击，找不到，抛出异常
            for black in self.black_list:
                eles = self.finds(*black)  # 元素订单，可能会查到多个，所以是finds,列表
                if len(eles) > 0:
                    # 对黑名单元素进行点击
                    eles[0].click()
                    return fuction(*args, **kwargs)  # 递归函数，处理好之后，返回自己
            raise e
    return base_fun
