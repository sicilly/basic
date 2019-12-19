a = 6
b = 100

# 解法一：使用其他变量
# c = a
# a = b
# b = c

# 解法二： 不使用其他的变量
# a = a + b
# b = a - b
# a = a - b

# 解法三： python专有
a, b = b, a

print(a)
print(b)
