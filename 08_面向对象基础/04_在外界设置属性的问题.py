class Cat:

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

# 在日常开发中，不推荐在类的外部给对象增加属性
tom.name = "Tom"

tom.eat()
tom.drink()
# 如果在运行时，没有找到属性，程序会报错
# tom.name = "Tom"

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()

