# 如果一个类中有__iter__方法且返回一个迭代器对象：
# 则我们称这个类创建的对象为可迭代对象
class Foo(object):
    def __iter__(self):
        return '迭代器对象（生成器对象，因为生成器内部类符合迭代器）'

obj = Foo() # obj是可迭代对象
"""
可迭代对象是可以使用for来进行循环，
在循环的内部其实是先执行__iter__方法，获取其迭代器对象，
然后再在内部指定这个迭代器对象的next功能，逐步取值
"""
# for item in obj:
#     pass

# 迭代器类 实例化时，会获得一个迭代器对象
class IT(object):
    def __init__(self):
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration()
        return self.counter


class Foo(object):
    def __iter__(self):
        # return '迭代器对象（生成器对象，因为生成器内部类符合迭代器）'
        return IT()

obj = Foo() #可迭代对象
for item in obj:
    """
    循环可迭代对象时，
    内部先执行obj.__iter__并获取迭代器对象:
    不断地执行迭代器对象的next方法
    """
    print(item)

"""
小贴士:dir(temp)，查看temp内部有哪些成员
dir()带参数时，返回参数的属性、方法列表
"""
temp = range(100000)
temp_1 = temp.__iter__()
print(dir(temp)) # 只有__iter__ 一个可迭代对象
print(dir(temp_1)) # 有__iter__ 和__next__ temp_2是一个迭代器对象 