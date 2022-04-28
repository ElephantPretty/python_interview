"""
*args 和 **kwargs 主要用于函数定义。

你可以将不定数量的参数传递给一个函数。不定的意思是：预先并不知道,
函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。
其实并不是必须写成 *args 和 **kwargs。  *(星号) 才是必须的.
你也可以写成 *ar  和 **k 。而写成 *args 和**kwargs 只是一个通俗的命名约定。

python函数传递参数的方式有两种：

位置参数（positional argument）
关键词参数（keyword argument）
*args 与 **kwargs 的区别，两者都是 python 中的可变参数：

*args 表示任何多个无名参数，它本质是一个 tuple
**kwargs 表示关键字参数，它本质上是一个 dict
如果同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前。


"""
def sum(*args):
    # 位置参数
    # 理解为传元组
    a = 0
    for n in args:
        a += n
    return a

print(sum(1,2,3,4,5))
tup = (1,2,3,4,5,6)
print(sum(*tup))

def register(**kwargs):
    # 关键字参数
    # 理解为传字典
    return kwargs
score={
    "麦叔":100,
    "Kevin":90,
    "Jason":95
}
print("第一种方式",register(**score))
print("第二种方式",register(**score,David=90,Sunhua=90.5))

def family(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

family(1,2,3,4,5,k=8,v=9)
