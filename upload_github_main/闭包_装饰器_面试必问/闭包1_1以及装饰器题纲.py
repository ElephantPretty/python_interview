"""
https://www.bilibili.com/video/BV1JW411i7HR?from=search&seid=12691595679482094786&spm_id_from=333.337.0.0
闭包：
内部函数对外部函数  作用域  里  变量  的引用【官方说法】
函数内的属性，都是有生命周期，生命周期都是在函数执行期间
闭包内的闭包函数[即内部函数，比如func1(num)]私有化变量，
其实完成了数据的封装，类似于面向对象

装饰器（闭包在装饰器中得到了使用）
@func1
def func():
    print('aaa')
    不影响原有函数的功能，还能添加新的功能
    @func1
    def myprint():
    myprint()其实等于func2() + myprint()
    普通装饰器：
    装饰器函数带参数：多一层包装来接收装饰器的参数
    被装饰的函数带参数：只需要在最内部函数传入参数即可【最easy】
"""

# 此时是真正意义上的闭包了
def func():# 外部函数
    a = 1 # 外部函数作用域里的变量
    print("this is func.")
    def func1(num):
        # 内部函数
        print("this is func1")
        print(num + a)
    return func1

func()# 运行外部函数，内部函数就被创建了
var = func() # 创建过程在func函数的执行过程中
# var == func1()
var(3) # 这个其实就相当于func1(),即实现了从外部调用内部函数，方式仅仅只是内部函数被return出来即可
del var