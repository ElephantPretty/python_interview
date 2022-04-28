"""
https://www.bilibili.com/video/BV1BT4y1P7nn?spm_id_from=333.337.search-card.all.click
迭代器定义:
1-类中定义了__iter__和__next__两个方法
2-__iter__方法需要返回对象本身,即self
3-__next__方法，返回下一个数据,如果没有数据了,则需要抛出一个StopIteration的异常
"""


class IT(object):
    """
    创建 迭代器类型:
    """
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration()
        return self.counter


"""
根据类实例化一个迭代器对象
"""
obj1 = IT()
# 1---------
# v1 = obj1.__next__()
# v2 = next(obj1)
# v3 = next(obj1) # 抛出异常
# 2----------
# v1 = next(obj1) # 使用python的内置函数来执行next,和__next__一样
# v2 = next(obj1)
obj2 = IT()
for item in obj2:
    # 1-首先会执行迭代器对象的__iter__方法并获取返回值，
    # 2-一直去反复的执行next(对象),每执行一次赋值给item
    # 我们平时用到的for循环，内部其实就依赖于迭代器
    print(item)
"""
迭代器对象支持通过next取值，如果取值结束则自动抛出StopIteration.
for循环内部在循环时,先执行__iter__方法，
获取一个迭代器对象，然后不断执行next取值
（有异常StopIteration则终止循环）
"""
# print(v2)