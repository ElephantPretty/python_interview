"""
https://www.bilibili.com/video/BV1BT4y1P7nn?spm_id_from=333.337.search-card.all.click
迭代器：
1-类中定义了__iter__和__next__两个方法
2-__iter__方法需要返回对象本身,即self
3-__next__方法，返回下一个数据，如果没有数据了，
则需要抛出一个stopIteration异常
"""
# 创建迭代器类型
class It(object):
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration
        return self.counter

# 根据类实例化一个迭代器对象
obj1 = It()
# obj1.__next__()
# obj1相当于一个可迭代对象iterator def next(iterator, default=None)
# next是python的一个内置函数

v1 = next(obj1)
print(v1)
v1 = next(obj1)
print(v1)

obj2 = It()
for item in obj2:
    # 首先会执行迭代器对象的__iter__方法，并获取返回值
    # 一直反复执行next(对象)
    print(item)



