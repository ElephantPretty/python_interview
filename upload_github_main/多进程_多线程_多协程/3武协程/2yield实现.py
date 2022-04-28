def func1():
    yield 1
    # 跳到func2这个函数去
    yield from func2()
    yield 2


def func2():
    yield 3
    yield 4


f1 = func1()
for item in f1:
    print(item)