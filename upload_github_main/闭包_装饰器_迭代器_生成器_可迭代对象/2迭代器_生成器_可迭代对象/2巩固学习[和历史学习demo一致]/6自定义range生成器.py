# class Foo(object):
#     def __iter__(self):
#         yield 1
#         yield 2
#
# obj = Foo()
# for item in obj:
#     print(item)
# 基于可迭代对象&生成器 实现range
class Xrange(object):
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        counter = 0
        while counter < self.max_num:
            yield counter
            counter += 1

obj = Xrange(100)
for item in obj:
    print(item)