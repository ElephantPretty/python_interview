def f(a,b):
    print(id(a),id(b))
    a += b
    return a
"""
python中一切皆对象，函数中传递的是对象的引用
形参假如改变,可能会影响到实参[如果传递的是可变对象]
"""
x = 1
print(id(x))
y = 2
print(id(y))
print(f(x,y))
print(x,y)
a = [1,2]
b = [3,4]
print(f(a,b))
print(a,b)
t = (10,20)
u = (30,40)
print(f(t,u))
print(t,u)