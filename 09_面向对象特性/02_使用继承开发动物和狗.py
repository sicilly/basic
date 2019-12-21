class Animal:

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


# 狗类继承动物类 子类拥有父类的所有方法和属性
class Dog(Animal):

    def bark(self):
        print("bark")


wangcai = Dog()

wangcai.run()
wangcai.eat()
wangcai.drink()
wangcai.bark()
wangcai.sleep()