import copy

a = "张小鸡"
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

print("赋值:id(b)->>>",id(b),a)
print("浅拷贝:id(c)->>>", id(c),c)
print("深拷贝:id(d)->>>", id(c),d)
"""
因为我们这里操作的是不可变对象，
Python 用引用计数的方式管理它们，
所以 Python 不会对值相同的不可变对象，
申请单独的内存空间。只会记录它的引用次数
"""

"""
浅拷贝和赋值在可变对象上的区别

发现没有，赋值就是对物体进行贴标签操作，
作用于同一物体。
而浅拷贝则会创建一个新的对象，
至于对象中的元素，它依然会引用原来的物体，我们再来看一段例子
"""
import copy
a = ["张小鸡"]
b = a
c = copy.copy(a)

print("a原地址->>",id(a))
print("赋值:id(b)->>>", id(b),b)
print("浅拷贝:id(c)->>>",id(c),c)

import copy
a = ["张小鸡"]
print("改变前,a内部的元素id：id([a])->>>",[id(x) for x in a])
c = copy.copy(a)
print("改变前,浅拷贝c内部的元素id:id([c])->>>",[id(x) for x in c])
a[0] = "姬无命"
print("改变后,a内部的元素id：id([a])->>>",[id(x) for x in a])
print("改变和,浅拷贝c内部的元素id:id([c])->>>",[id(x) for x in c])