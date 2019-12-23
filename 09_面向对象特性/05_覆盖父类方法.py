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

    # 重写
    def bark(self):
        print("哮天犬在叫")


# 创建一个哮天犬的对象
xtq = XiaoTianQuan()

# 如果在子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法，不会调用父类封装的方法
xtq.bark()
