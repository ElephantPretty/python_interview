"""
一个程序中的配置文件就可以写成单例模式
"""
import threading
import time


class Singleton():

    instance = None

    def __init__(self,name):
        self.name = name

    def __new__(cls,*args,**kwargs):
        """
        __new__(cls)方法
        __new__(cls)必须要有一个参数cls,代表着要实例化的类，而且必须要有返回值，返回实例化出来的实例对象.
        """
        if cls.instance == None:
            # 创建空对象
            obj = object.__new__(cls)
            # 这句话十分关键，假如第一个执行的线程速度不够快，
            # 就会有问题出现！
            time.sleep(0.1)
            cls.instance = obj
        return cls.instance

# 1正常情况下单线程-单例模式这样写法是无问题的
# s1 = Singleton('张三')
# print(s1)
# print(s1.name)
# s2 = Singleton('张三')
# print(s2.name)
# print(Singleton.instance)
# 2多线程情况下这样的单例模式写法会有问题
def task():
    obj = Singleton('x')
    print(obj)

for i in range(101):
    t = threading.Thread(target=task)
    t.start()

