"""
文件指针标记从哪个位置开始读取数据
第一次打开文件时，通常文件指针会指向文件的开始位置
当执行了read方法后，文件指针会移动到读取内容的末尾
"""

# 1. 打开文件
file = open("README")

# 2. 读取文件内容
text = file.read()
print(text)
print(len(text))

print("-" * 50)

# 第一次读取后，文件指针移动到了文件末尾，再次调用不会读取到任何内容
text = file.read()
print(text)
print(len(text))

# 3. 关闭文件
file.close()
