xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75,
            "weight": 75
            }

# 1. 取值
print(xiaoming["name"])

# 2. 增加/修改
# 如果key不存在，会新增键值对
xiaoming["ha"] = "hahahha"
# 如果key存在，会修改已经存在的键值对
xiaoming["ha"] = "xiugaila"

# 3. 删除
xiaoming.pop("ha")

print(xiaoming)