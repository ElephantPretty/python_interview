symbols = 'abcdhjkl'
codes = []
for symbol in symbols:
    # ord即单个字符转ascii数值 我们应当知道a的arcii值为97
    codes.append(ord(symbol))
print(codes)

"""
列表推导式应当尽量保持简短，若超过两行，应当思考
"""
codes = [ord(symbol) for symbol in symbols]
print(type(codes))
print(codes)

"""
列表推导式可帮助我们把一个序列或是其他可迭代类型中的元素过滤或是加工，然后在新建一个列表。
python内置的filter和map组合起来也能完成，可读性差
"""
symbols = 'abcdhjkl'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 97]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 97, map(ord, symbols)))
print(beyond_ascii)

"""
map filter,reduce练习
1-map(func,seq), 
将序列seq中的元素取出来，
依次放到Func函数，将结果以列表形式返回，支持多参数
python3返回迭代器
2-filter就像一个if else情况，过滤不满足条件的数据
3-reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
"""

# map-例题1
def add(x):
    return x + 3


a = [1, 2, 3, 4]

list_map = map(add, a)
for i in list_map:
    print(i)

# map-例题2-法一
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list_temp = map(lambda x: x * 10, list1)
# for i in list_temp:
#     print(i)
# print(list_temp)
# print(type(list_temp)) #map类型
list_result = map(lambda x, y: x + y, list_temp, list2)
# for i in list_result:
#     print(i)
result = sum(list_result)
print(result)

# map-例题2-法二
list3 = [x * 10 + y for x, y in zip(list1, list2)]
print(sum(list3))

#filter-例题1-过滤出1~100中平方根是整数的数：
#sqrt() 方法返回数字x的平方根。9的开根号是3
import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0

tmp_list = filter(lambda x: math.sqrt(x) % 1 == 0, range(1, 101))
new_list = list(tmp_list)
print(new_list)

from functools import reduce
#reduce-例题1
def add(x, y):
    return x + y
sum1 = reduce(add, [1,2,3,4,5])
sum2 = reduce(lambda x, y:x + y, [1,2,3,4,5])
print(sum1)
print(sum2)
sum3 = reduce(lambda x, y:x * y, [1,2,3,4,5])
print(sum3)