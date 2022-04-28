class It(object):
    """
    实现了__iter__和__next__
    是一个迭代器类
    """
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        # 返回一个迭代器对象
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration()
        return self.counter

class Foo(object):
    """
    类中实现了__iter__方法且返回可迭代对象
    则类实例化创建的对象为可迭代对象！
    """
    def __iter__(self):
        return It()


obj = Foo() # obj是一个可迭代对象
for item in obj:
    """
    先执行__iter__，获取一个迭代器对象
    在不断执行对象的next方法
    """
    print(item)

