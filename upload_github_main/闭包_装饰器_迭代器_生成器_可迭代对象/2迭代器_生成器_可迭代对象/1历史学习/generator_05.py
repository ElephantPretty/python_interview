class Foo(object):
    """
    承接02, 04，用生成器来实现for,其实本质也符合可迭代对象的定义
    """
    def __iter__(self):
        yield 1
        yield 2


# obj = Foo()
# for item in obj:
#     print(item)


class Xrange(object):
    """
    基于可迭代对象&生成器 实现：自定义range
    """
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        counter = 0
        while counter < self.max_num:
            yield counter
            counter += 1

obj = Xrange(100)
for item in obj:
    print(item) # 0-99
