class Animal:

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("fly")

    def bark(self):
        # 1. 针对子类特有的需求，编写代码
        print("神一样的叫唤")
        # 2. 使用super(). 调用原本在父类中封装的方法
        super().bark()
        # 3. 增加其他子类的代码
        print("$%^^&&*")

# 创建一个哮天犬的对象
xtq = XiaoTianQuan()

# 如果在子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法，不会调用父类封装的方法
xtq.bark()
