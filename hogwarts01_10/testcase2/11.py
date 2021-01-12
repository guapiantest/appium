from selenium.webdriver.common.by import By





def b(fun):
    def fuc(*args,**kwargs):
        print("a1")
        fun(*args,**kwargs)
        print("a2")
    return fuc

@b
def a():
    print("a")


def test():
    a()
