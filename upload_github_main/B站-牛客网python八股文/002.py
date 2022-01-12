"""
题目2
考虑一下python代码，如果运行结束，命令行中的运行结果是什么?
"""
# l1 = []
# for i in range(3):
#     l1.append({'num': i})
# print(l1)
# l2 = []
# a = {'num': 0}
# for i in range(3):
#     # 字典是个可变类型，不仅仅改了a字典，他把列表里面的a也改了
#     # 不需要重新赋值
#     a['num'] = i
#     l2.append(a)
# print(a)
# print(l1)
# print(l2)
"""
解析 因为字典是可变类型，修改后变量不用重新赋值
也就是说所有内存里面的a这个变量对应的字典都会一起改变
"""
a = {'num':0}
l3 = [a,a,a,a]
a['num'] = 3
print(l3)