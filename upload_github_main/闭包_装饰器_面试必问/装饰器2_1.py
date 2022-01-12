def func1(func):# 外部闭包函数的参数是被装饰的函数对象
    def func2():# 这是一个闭包函数，它将func2以及里面的东西返回了
        """
        之前写闭包的时候，内部函数没有返回值，
        但是现在这个内部函数会有返回值
        :return:
        """
        print('aaabbb')
        return func() # 返回了外部函数接收的参数，被装饰函数的调用---这里其实是myprint()被调用了
    return func2

"""
return func 返回了集装箱，函数对象，函数名
return func() 返回的是一个函数调用
第一步：func1将把被装饰的函数myprint传入到形参func中。
第二步：func1会返回func2
第三步：myprint会调用,myprint()--->实际上为func2()，
此时内部执行完'aaabbb'后，在进而执行func(),即myprint(),
由于闭包
1-func1(myprint)() 接收被装饰的函数作为参数，而且还要继续调用一次
2-func1(myprint)执行完成后会返回->func2
3-fun2()内部函数调用时会首先调用aaabbb,func()即传递进来的myprint()
"""
@func1 # 专门接收一个函数对象
def myprint():
    print('你好，我是大象')

myprint() # func1(myprint)()