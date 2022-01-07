"""
题目3
求两个集合的交集，并集和差集,说明结果的原因
set1 = {2,2,2,True,4+3j}
set2 = {1,2,2,False,4+3j}
"""
set1 = {2, 2.2, True, 4+3j}
set2 = {1, 2.2, False, 4+3j}
# print(int(True))--1
"""
交集（肉眼看到的相同元素是2.2和4+3j 还出现了1，是因为True转换成int类型的值是1,所以还有1）
set1去找set2里面是否有相同的元素 找到set2的1 发现set1里面没有1 自动把True转化为1  依赖于set2 就相当于是排序比较
"""
# print(set1 & set2)--{1, 2.2, (4+3j)}
"""
求交集，以第二个集合为优先级
set2去找set1里面是否有相同的元素 找到set1的True 发现set2里面没有True 依赖于set1 自动把1转化为True
"""
# print(bool(1))--True
# print(bool(2.2))--True
# print(set2 & set1)--{True, 2.2, (4+3j)}
"""
求并集，所有元素都要，但是相同的元素需要消掉，比如1 和 True
先展示set1里面的元素，因为开始展示了set的True 然后去找sett2里面不同的元素
所以他认为1和True是一样的 所以1就被当做和True相同元素去看了，不会展示
以第一个集合为优先级
"""
# print(set1 | set2)--{False, True, 2, 2.2, (4+3j)}
# print(set2 | set1)--{False, 1, 2.2, 2, (4+3j)}
"""
求差集 (set1做减数的时候，set1减去他们的交集，就是差集的结果)
"""
# print(set1 - set2)--{2}
# print(set2 - set1)----{False}

# funca = lambda x : x + 1 if x == 1 else 0
# a = 1
# print(a)
# print(id(a))
# a = a + 1
# print(a)
# print(id(a))
# print(funca(1))
# print(funca(2))


#https://www.cnblogs.com/gcgc/p/11426478.html-----python:动态参数*args
# *args用来将参数打包成tuple给函数体调用
# def func(*args):
#     """
#     *表示接收任意个数量的参数，调用时会将实际参数打包为一个元祖传入实参
#     :param args:
#     :return:
#     """
#     print(args)
#     print(type(args))
#     for i in args:
#         print(i)
# func({'name':'book'}, 123, 'hello', ['a','b','c'])
# func(*['a', 'b', 'c'])
# **kwargs 打包关键字参数成dict给函数体调用
# def function(arg, *args, **kwargs):
#     print(arg, args, kwargs)
# https://www.cnblogs.com/yunguoxiaoqiao/p/7626992.html
# function(6, 7, 8, 9, a = 1, b = 2, c = 3)

#可变与不可变 https://blog.csdn.net/S1433972007LJ/article/details/85954953
# number = 1
# print(id(number), type(number))
# number += 1
# print(id(number), type(number))
#
# name = 'Super Man超人'
# print(id(name), type(name))
# name = 'Iron Man钢铁侠'
# print(id(name), type(name))
#
# tuple_data1 = (1, 'Hello')
# print(id(tuple_data1), type(tuple_data1))
# tuple_data2 = ([2,3], (5,6))
# tuple_data1 = tuple_data1 + tuple_data2
# print(id(tuple_data1), type(tuple_data1))
# print(tuple_data1)
#
# list_data = [1, 'q', 'qwer', True]
# print(id(list_data), type(list_data))
# list_data.append('djx')
# print(id(list_data), type(list_data))
#
# dict_data = {2:1, 'key2':'djx', 'key3':'li'}
# print(id(dict_data), type(dict_data))
# dict_data['key4'] = 'haha'
# print(id(dict_data), type(dict_data))
#
# set_data = {1, 'd', '34', '1', 1}
# print(id(set_data), type(set_data))
# set_data.add('djx')
# print(id(set_data), type(set_data))


