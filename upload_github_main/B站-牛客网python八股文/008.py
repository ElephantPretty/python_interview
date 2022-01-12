"""
题目8--面试问了基础的匿名函数
salaries = {
    'aaa':30000000,
    'bbb':1000000000,
    'ccc':2000
}
求薪资最高的那个人名
"""
#法1
salaries = {
    'aaa':30000000,
    'bbb':1000000000,
    'ccc':2000
}
# temp_name = 'zhangsan'
# max_number = 1
# for key,value in salaries.items():
#     if max < value:
#         temp_name = key
#         max_number = value
# print(temp_name)
#法2
"""
求薪资最高的那个人名：即比较的value,但取结果是key
默认比较的是字典的key 如果比较value呢？
"""
# res = max(salaries)
# print(res)
# 比较value
# def func(name):
#     return salaries[name]

"""
max(字典, key=函数名)
print(func('bbb'))
改变它的比较逻辑
自动比较返回值(value)，返回的依旧是key
用匿名函数(只用一次，一次性杯子)来优化
"""
res1 = max(salaries, key=lambda name:salaries[name])
print(res1)

"""
个人 lamba函数使用 匿名函数
"""
# g = lambda x: x+1
# g(1)
#
#
# def is_odd(n):
#     return n % 2 == 1
#
#
# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# filter_foo = filter(lambda x: x % 2 == 1, foo)
# print(list(filter_foo))


