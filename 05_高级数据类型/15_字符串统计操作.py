hello_str = "hello hello"

# 1. 统计长度
print(len(hello_str))

# 2.统计某一个子字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("A"))

# 3. 某一个子字符串出现的位置
print(hello_str.index("llo"))
# 如果子字符串不存在，程序会报错
