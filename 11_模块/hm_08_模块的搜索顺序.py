"""
1. 搜索当前目录指定模块名的文件，如果有就直接导入
2. 如果没有，再搜索系统目录

在开发时，给文件起名，不要和系统的模块文件重名

"""


import random

print(random.__file__)

rand = random.randint(0, 10)

print(rand)
