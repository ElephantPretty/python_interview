"""
承接-03
基于可迭代对象&迭代器实现:自定义range
"""
class IterRange(object):
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
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        # 返回一个迭代器
        return IterRange(self.max_num)


obj = Xrange(100) # 一个可迭代对象
for item in obj:
    print(item) # 0-99,这就是平时用到的for,基于可迭代对象


