"""
一个程序中的配置文件就可以写成单例模式
"""
import threading
import time

class Singleton():

    instance = None
    lock_object = threading.RLock()

    def __init__(self,name):
        self.name = name

    def __new__(cls,*args,**kwargs):
        """
        __new__(cls)方法
        __new__(cls)必须要有一个参数cls,代表着要实例化的类，而且必须要有返回值，返回实例化出来的实例对象.
        """
        # 这句话会让效率高一些
        if cls.instance:
            return cls.instance
        # 使用加锁来解决
        with cls.lock_object:
            if cls.instance:
                return cls.instance
            obj = object.__new__(cls)
            # 这句话十分关键，假如第一个执行的线程速度不够快，
            # 就会有问题出现！
            time.sleep(0.1)
            cls.instance = obj
            return cls.instance

# 多线程情况单例模式解决-加锁
def task():
    obj = Singleton('x')
    print(obj)

for i in range(101):
    t = threading.Thread(target=task)
    t.start()

