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
        print("bark")


class XiaoTianQuan(Dog):
    def fly(self):
        print("fly")


class Cat(Animal):
    def catch(self):
        print("抓老鼠")


# 创建一个哮天犬的对象
xtq = XiaoTianQuan()

xtq.fly()
xtq.bark()
xtq.sleep()

# xtq和Cat类没有继承关系，xtq不能抓老鼠
