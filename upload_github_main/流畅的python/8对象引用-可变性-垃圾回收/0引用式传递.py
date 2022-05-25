"""
https://my.oschina.net/leejun2005/blog/145911
"""
# values = [0,1,2]
# # values[1] = values
# # 生成对象的拷贝或者是复制序列,不再是引用和共享变量,
# # 此方法只能顶层复制--潜复制
# values[1] = values[:]
# print(values)
import copy

a = [0,[1,2],3]
# [0,[1,2],3]
# b = a[:]
# 用深复制来解决
b = copy.deepcopy(a)
a[0] = 8
a[1][1] = 9
print(a)
print(b)