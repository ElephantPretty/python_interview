# 基于可迭代对象&迭代器实现:自定义range
class IterRange(object):
    """
    迭代器
    1-实现__iter__和__next__方法
    2-__iter__返回对象本身
    3-__next__需要返回下一个数据，没有则抛出异常

    """
    def __init__(self, num):
        self.num = num
        self.counter = -1


    def __iter__(self):
        return self


    def __next__(self):
        self.counter += 1
        if self.counter == self.num:
            raise StopIteration()
        return self.counter


class Xrange(object):
    # 因为实现__iter__方法，且返回的是可迭代对象
    # 作用：其实例化对象是可迭代对象
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        return IterRange(self.max_num)

obj = Xrange(100)
for item in obj:
    print(item)
