"""
被装饰的函数携带参数，格式比较简单，
不需要在外层加函数--可与装饰器携带参数作比较
"""

def func1(func):
    def func2(x, y):
        x+=5
        y+=5
        return func(x,y)
    return func2



@func1
def my_sum(a, b):
    """
    需求是在原有基础上实现a += 5, 且这个代码不能写在my_sum函数中实现
    方案：我们可以使用装饰器解决
    :param a:
    :param b:
    :return:
    """
    # return a + b
    print(a + b)

my_sum(1, 2)