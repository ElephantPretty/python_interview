# class Dog(object):
#     name = "stupid_dog"
#
#     def __init__(self,name):
#         self.name = name
#
#     # 类方法只能访问类变量，不能访问实例变量
#     @classmethod
#     def eat(self):
#         # 不加 实例本身 <__main__.Dog object at 0x000001D0418DFCF8>
#         # 加了classmethod 类本身 <class '__main__.Dog'>
#         print("-->", self)
#         print("dog %s is eating..."%self.name)
#
#     @classmethod
#     def run(cls):
#         # 类本身
#         print(cls)
#
# d = Dog("Mjj")
# d.eat()
# d.run()
"""
@classmethod这个源码用的多，实际少
但是flask经常是这个
"""
class Student(object):

    __stu_num = 0

    def __init__(self, name):
        self.name = name
        # 你认为给类变量加1，实际上是给实例变量进行赋值
        # self.stu_num += 1
        # Student.stu_num +=1
        # print("生成了一个新学生", name,self.stu_num)
        self.add_stu(self)

    @classmethod
    def add_stu(cls, obj):
        # obj stands for self instance
        if obj.name:
            cls.__stu_num += 1
            print("生成了一个新学生", cls.__stu_num)

s1 = Student("A1")
s2 = Student("A2")
s3 = Student("A3")
# 此时判断后，外部调用类方法不能计数+1
Student.add_stu()