"""
 row    col
第一行 循环1次
第二行 循环2次
……
第五行 循环5次
"""
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*",end="")
        col += 1
    print("")
    row += 1
