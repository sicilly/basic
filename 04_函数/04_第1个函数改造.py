name = "小明"

# python 解释器知道下方定义了一个函数


def say_hello():
    """打招呼（我是函数的文档注释）"""

    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)

# 只有在程序中主动调用函数，才会让函数执行 ctrl+Q查看函数文档注释
say_hello()

print(name)
