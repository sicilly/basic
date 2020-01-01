"""
在开发中，可以在主函数中增加异常捕获
而在主函数中调用其他函数，只要出现异常，都会传递到主函数的异常捕获中
这样就不需要在代码中，增加大量的异常捕获，能够保证代码的简洁

"""


def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except Exception as result:
    print("未知错误 %s" % result)
