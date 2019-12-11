def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    """ 打印多行分割线

    :param char: 分割字符
    :param times: 重复次数
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines("-", 20)
