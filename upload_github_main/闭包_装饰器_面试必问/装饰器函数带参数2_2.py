"""
加入装饰器时若需要函数带有参数时该如何写？1-12

"""
def arg_func(sex): # 这是特意为了接收带参数的对象,而添加的一层,sex是被装饰函数携带的参数
    def func1(b_func):
        def func2():
            if sex == 'man':
                print('你不可以生娃')
            if sex == 'woman':
                print('你可以生娃')
            return b_func()
        return func2
    return func1

"""
执行分析过程：
@arg_func(sex='man')()->arg_func(man(sex='man'))()
func1(man(sex='man')) 这里是执行内部闭包函数func1()
func1()会执行闭包函数func2()，里面包含性别判断和被装饰的函数调用
"""


@arg_func(sex='man')
def man():
    print('好好上班.')


@arg_func(sex='woman')
def woman():
    print('好好上班.')

man()
woman()