name_list = ["张三","李四","王五","张三"]

# 统计列表中元素的总数
list_len = len(name_list)
print(list_len)

# count
count = name_list.count("张三")
print(count)

# 从列表中删除第一次出现的数据，如果数据不存在会报错
name_list.remove("张三")