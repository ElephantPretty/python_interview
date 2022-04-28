"""
    学习总结：22-1-10

    可迭代对象：一般为数据容器，且保留 迭代接口__iter__。
    迭代器：类，实现了__iter__ 和 __next__接口的类。
    生成器：函数，通过yield遍历元素。

    1、__iter__方法是留给程序获得 迭代对象 iter()
    2、获得迭代对象后，通过__next__ 或next()遍历元素。

"""
"""
常见的数据类型:
v1 = list([11,22,33,44])
v1是一个可迭代对象，
元组,字典，列表都是可迭代对象
因为在列表中声明了一个__iter__方法并且返回一个迭代器对象。
"""
v1 = list([11,22,33,44]) # 可迭代对象
print(dir(v1)) # __iter__
v11 = v1.__iter__() # 迭代器对象
print(dir(v11)) # __iter__ __next__
print(next(v11))
print(v11.__next__())

"""
科学代码来判断一个东西是否是可迭代对象
"""
from collections.abc import Iterator,Iterable

v1 = [11, 22, 33] # 内部有一个__iter__,应当是属于可迭代对象
print(isinstance(v1, Iterator)) # False 判断是否是迭代器：判断依据是__iter__和__next__
print(isinstance(v1, Iterable)) # True
# 判断是否可迭代(即是否一个可迭代对象-这是不准确的，因为也有可能是一个迭代器对象):判断依据是是否有__iter__且返回迭代器对象

v11 = v1.__iter__() # 里面有__iter__和__next__，属于迭代器定义
print(isinstance(v11, Iterator)) #是一个迭代器

v1 = [11, 22, 33]
print(isinstance(v1, Iterable)) # True,判断依据是是否具有__iter__且返回迭代器对象
v21 = v1.__iter__()
print(isinstance(v21,Iterable)) # True,判断依据是是否具有__iter__且返回迭代器对象
# 判断是否可迭代(即是否一个可迭代对象-这是不准确的，因为也有可能是一个迭代器对象):判断依据是是否有__iter__且返回迭代器对象
# print(isinstance(v2, Iterable))
# print(isinstance(v2, Iterable))