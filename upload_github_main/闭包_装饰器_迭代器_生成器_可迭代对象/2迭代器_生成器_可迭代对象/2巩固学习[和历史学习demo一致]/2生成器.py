# 创建生成器函数
"""
在 Python 中，使用了 yield 的函数被称为生成器（generator）
在调用生成器运行的过程中，
每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
返回 yield 的值,
并在下一次执行 next() 方法时从当前位置继续运行。

有yield的函数则返回一个可迭代的 generator（生成器）对象
"""
def func():
    yield 1
    yield 2

"""
创建生成器对象(内部是根据生成器类generator创建的对象)，
生成器类的内部也生命了:__iter__和__next__方法

依据迭代器的规定来看，
生成器类其实也是一种特殊的迭代器类
生成器其实是一个特殊的迭代器

生成器对象=特殊的迭代器对象
"""

obj1 = func()
v1 = next(obj1)
print(v1)
v2 = next(obj1)
print(v2)
# v3 = next(obj1)
# print(v3)

obj2 = func()
for item in obj2:
    print(item)