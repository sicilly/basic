class Cat:
    """这是一个猫类"""

    def __init__(self):
        print("初始化方法")

        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat()

tom.eat()
