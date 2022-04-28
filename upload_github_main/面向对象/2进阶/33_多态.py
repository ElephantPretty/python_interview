"""
什么是多态？
多态顾名思义多种状态，在python中，
不同的对象调用同一个接口，表现出不同的状态，称为多态。

如何实现多态？
1-继承：多态必须发生在子类和父类之间
2-重写：子类重写父类方法
示例1：加法运算符的多态
示例2：多态len()函数

多态用处：
一是增加程序的灵活性，
二是增加程序的可扩展性
"""

class Cat(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print("我是一只猫,我的名字是%s"%(self.name))

    def make_sound(self):
        print("喵喵喵")

class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print("我是一只狗,我的名字是%s"%(self.name))

    def make_sound(self):
        print("汪汪汪")


# cat1 = Cat("Kitty",2.5)
# dog1 = Dog("Snow",3)
#
# for animal in (cat1,dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()
from math import pi
class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "我是一个二维的形状"

    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self,length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "正方形的每个角都是90度"

class Circle(Shape):
    def __init__(self,radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

def view(obj):
    print(obj.area())

if __name__ == "__main__":
    a = Square(4)
    b = Circle(7)
    view(a)
    view(b)
# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(b.area())
# print(a.fact())
