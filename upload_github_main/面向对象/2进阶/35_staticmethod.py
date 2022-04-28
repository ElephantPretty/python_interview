"""
可以看成是静态方法已经跟这个类没关系了，相当于已经脱离了这个类，
是一个完全独立的函数，
只是调用的时候必须通过这个类, 或者为了规范代码而将函数放到类中
类中定义函方法 PyCharm 提示Method xxx may be ‘static’，
原因是该方法不涉及对该类属性的操作，编译器建议声明为@staticmethod，面向对象思想体现

看起来像是被家族[类]声明断绝金钱关系的富家子弟[静态方法],
富家子弟只是和家族名存实亡[表面还是走类的形式来调用]，实际没啥关系

"""
import time
class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        print("静态方法-我和这个类【不使用其中的类变量,实例变量。。。,self都没有】看起来没啥关系")
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

date = Date.now()
print(date.year,date.month,date.day)
date = Date(1999,12,12)