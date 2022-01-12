"""
若定义一个函数，
其中出现关键字yield，
则这个函数叫生成器函数
生成器内部声明了__iter__,__next__方法
根据迭代器定义，生成器其实也是一种特殊的迭代器
教程-
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。
"""


def func():
    """
    创建生成器函数
    :return:
    """
    yield 1
    yield 2

# 创建生成器对象(内部是根据生成器类generator创建的对象),
# 生成器内部也声明了:__iter__，__next__方法
obj1 = func()
v1 = next(obj1)
print(v1)
v2 = next(obj1)
print(v2)
# v3 = next(obj1)
# print(v3)

obj2 = func()
# 从迭代器的规定来看，
# 其实生成器也是一种特殊的迭代器类（生成器也是一个特数的迭代器）
for item in obj2:
    print(item)




# 练习生成器
# import sys
#
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         print("counter = ", counter)
#         # print("yield返回的a = ", a)
#         yield a
#         a, b = b, a + b
#         counter += 1
#
# f = fibonacci(10)
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()