#! D:\Anaconda3\python.exe

import cards_tools
# 无限循环，由用户主动决定什么时候退出循环
while True:

    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3 针对名片的操作
    # 字符串判断
    # 使用in针对列表判断，避免使用or拼接复杂的逻辑条件
    # 没有使用int转换用户输入，可以避免一旦用户输入的2
    # 不是数字，导致程序运行出错
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
        # 如果在开发程序时，不希望立刻编写分支内部的代码
        # 可以使用pass关键字，表示一个占位符，能够保证程序的代码结构正确
        # 程序运行时，pass关键字不会执行任何操作
    # 其他内容 输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")
