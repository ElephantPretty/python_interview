def func():
    msg = '111'
    def func1():
        print(msg)
    return func1

"""
1-理解闭包
闭包即内部函数调用外部函数作用域里面的变量
比如func1就是一个闭包函数
"""
func()()# 这里实际上是func1()

"""
2-装饰器
fn是被装饰的目标函数
2.1-仅仅只是传递函数名的装饰器[基本不会用到]
2.2-装饰带有参数的函数
2.3-装饰带有返回值的函数
2.4-装饰参数不确定的函数[可归类到装饰带有参数的函数里面]
2.5-装饰器本身携带参数
"""
def decorator(fn):
    def wrapper():
        print("添加的功能,装饰不带有参数的函数")
        return fn()
    return wrapper

@decorator
def test():
    print("原有功能")


test()# 实际上是decorator(test)

def decorator1(fn):
    def wrapper(n1,n2):
        print("添加的功能，装饰带有参数的函数")
        return fn(n1,n2)
    return wrapper

@decorator1
def test1(a,b):
    print("a+b=%s"%(a+b))
    print("原有功能")


test1(1,2)# 实际上是decorator1(test1(1,2))

def decoretor2(fn):
    def wrapper():
        print("添加的功能，装饰带有返回值的函数")
        res = fn()
        return res
    return wrapper

@decoretor2
def test2():
    print("原有功能")
    return "返回值001"

a = test2() # 实际是decorator2(test2)
print(a)


def decorator3(fn):
    def warpper(*args,**kwargs):
        print("添加的功能，装饰不定长参数的函数")
        return fn(*args,**kwargs)
    return warpper

@decorator3
def test3(n1,n2,n3):
    print("原有功能")
    print(n1+n2+n3)


test3(1,2,3)# 实际上是decorator1(test1(1,2,3))

def decorator4(home):
    def func_1(fn):
        def wrapper(*args,**kwargs):
            print("装饰器本身携带参数")
            print("目前家在%s"%(home))
            return fn(*args,**kwargs)
        return wrapper
    return func_1

@decorator4(home='wuhan')
def test4(n1,n2,n3):
    print("原有功能")
    print(n1+n2+n3)

# test3(1,2,3)=decorator3(home="武汉")(test(1,2,3))()
"""
1-先调用decorator3(home="wuhan")
2-执行func_1(test(1,2,3)) # 到这里其实就和前面的装饰器一样
3-执行wrapper
4-执行test(1,2,3)
"""
test4(1,2,3)





