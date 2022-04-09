# class Student(object):
#     def __init__(self,name):
#         self.name = name
#         print("init hahaha")
#
#     def __new__(cls,*args,**kwargs):
#         # cls代表类本身
#         # 负责执行__init__
#         # new是负责调用init的，进行一些实例初始化前的工作
#         print(cls,args,kwargs)
#         return object.__new__(cls)
#
# p = Student("Alex")
"""
23种设计模式之单例模式
"""
class Printer():
    tasks = []
    instance = None # 存放一个实例对象
    def __init__(self,name):
        self.name = name

    def add_task(self,job):
        self.tasks.append(job)
        print("[%s]添加任务[%s]到打印机，总任务数[%s]"%(self.name,job,len(self.tasks)))

    def __new__(cls,*args,**kwargs):
        # 只有一次实例化的石猴，正常进行，后面每次实例化，并不创建一个新实例
        if cls.instance is None:
            # 进行正常的实例化
            obj = object.__new__(cls)
            # 实例化的对象存下来
            cls.instance = obj
        # 以后的每次实例化，直接返回第一次的实例对象
        return cls.instance


p1 = Printer("Word app")
p2 = Printer("pdf app")
p3 = Printer("excel app")

p1.add_task("word file")
p2.add_task("pdf file")
p3.add_task("excel file")