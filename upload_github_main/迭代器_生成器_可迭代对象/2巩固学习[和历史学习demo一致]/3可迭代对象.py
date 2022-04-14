"""
如果一个类中有__iter__方法且返回一个迭代器对象
则我们称这个类创建的对象为可迭代对象

"""

class Foo(object):
    def __iter__(self):
        # 因为生成器是特殊的迭代器
        return '迭代器对象[生成器对象]'

obj = Foo() # obj是可迭代对象
"""
可迭代对象可以使用for来进行循环
循环的内部其实是先执行__iter__方法，
获取其迭代器对象，然后再在内部指定这个迭代器对象的next功能，逐步取值

"""
for item in obj:
    pass