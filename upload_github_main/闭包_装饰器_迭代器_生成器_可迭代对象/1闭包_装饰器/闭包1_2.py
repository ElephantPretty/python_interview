mylist = [1,2,3,4,5]


def func(obj):
    """
    外部函数返回一个内部函数，就是一个闭包
    """
    print('func:',obj)


    def func1():
        obj[0] += 1
        print("func1:", obj)
    return func1


var = func(mylist)
# 因为没有执行del 所以var和里面的东西一直存在
var()
var()
var()

