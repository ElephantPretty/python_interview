"""
python中有多种方式可以实现协程
比如greenlet和yield
这样写的代码没有意义
这种来回切换执行,使程序的执行速度更慢了[相比较与串行]
"""
from greenlet import greenlet

# def func1():
#     # 第二步,输出1
#     print(1)
#     # 第三步,切换到func2函数
#     gr2.switch()
#     # 第六步,输出2
#     print(2)
#     # 第七步,切换到func2函数,从上一次执行的位置继续向后执行
#     gr2.switch()
#
# def func2():
#     # 第四步,输出3
#     print(3)
#     # 第五步,切换到func1函数,从上一次执行的位置继续向后执行
#     gr1.switch()
#     # 第八步,输出4
#     print(4)
#
# gr1 = greenlet(func1)
# gr2 = greenlet(func2)
# # 第一步,去执行func1函数
# gr1.switch()

# 这个也能实现协程[切换]
def func1():
    yield 1
    yield from func2()
    yield 2

def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:
    """
    1
    func2()-- 3 4
    2
    """
    print(item)