# 注意：在开发时，应该把模块中所有全局变量
# 定义在所有函数上方，就可以保证所有的函数
# 都能够正常的访问到每一个全局变量了
num = 10


def demo():
    print("%d" % num)
    print("%s" % title)
    # print("%s" % name)


# 再定义一个全局变量
title = "it"

demo()

# 再定义一个全局变量 会报错
# name = "小明"
