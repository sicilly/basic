xiaoming = {"name": "小明",
            "age": 20,
            }

# 1. 统计键值对数量
print(len(xiaoming))

# 2. 合并字典
temp = {"age": 18,
        "gender": True,
        "height": 1.75,
        "weight": 75
        }
# 如果被合并的字典中包含
xiaoming.update(temp)


# 3. 清空字典
xiaoming.clear()

print(xiaoming)
