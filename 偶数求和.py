# 计算 0 ~ 100 之间所有偶数的累计求和结果
result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)

        result += i
    i += 1
print("0 ~ 100 之间所有偶数的累计求和结果= %d " % result)
