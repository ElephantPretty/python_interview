"""
@property 属性方法
属性方法的作用就是通过@property把一个方法变成一个静态属性
实例名.方法
"""

# class Foo(object):
#     def __init__(self,name):
#         self.name = name
#
#     def func(self):
#         print("%s:基本方法"%self.name)
#
#     @property # pro = property(pro)
#     def pro(self):
#         print("%s:属性方法"%self.name)
#
#
# f1 = Foo("elephant111")
# f1.func()
# # 调用
# f1.pro

"""
@property属性方法 封装类中的方法，给用户更加简单的调用方式，隐藏具体的实现细节。
@method.getter 获取属性
@method.setter 设置属性, 可以写更多逻辑（比如格式转换，类型判断），并提醒其他人这里面可能有magic
@method.deleter 删除属性
"""
class Foo(object):
    def __init__(self,name):
        self.__name = name

    def func(self):
        # print("%s:基本方法"%self.__name)
        pass

    @property # pro = property(pro)
    def pro(self):
        return self.__name

    @pro.setter
    def pro(self,name):
        self.__name = name


    @pro.getter
    def pro(self):
        return self.__name

    @pro.deleter
    def pro(self):
        del self.__name
        # print()


f1 = Foo("elephant111")
print(f1.pro)
f1.pro="张三"
print(f1.pro)
del f1.pro
# 删除之后是无法显示__name的
print(f1.pro)