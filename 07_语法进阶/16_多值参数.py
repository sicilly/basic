# 参数名前增加一个*可以接收元组
# 参数名前增加两个*可以接收字典


def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


demo(1, 2, 3, 4, 5, name="小明", age=18)
