def yinyong(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))


# 1. 定义一个数字的变量
a = 10

# 数据的地址本质上就是一个数字
print("a变量保存数据的内存地址是 %d" % id(a))

# 2. 调用yinyong函数，本质上传递的是实参保存数据的引用，而不是实参保存的数据
yinyong(a)
