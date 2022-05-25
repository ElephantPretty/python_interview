

f = lambda x, y : x * y
a = map(lambda x, y:x * y, range(3), range(3))
# print(range(3))
# print(type(range(3)))
# b = list(a)
# print(b)
list_demo = [1,2,3,4,5]
new_list = map(lambda x:x*2,list_demo)
# print(list(new_list))
list_demo = filter(lambda x: x % 2 == 0, list_demo)
# print(list(list_demo))
import functools
list_demo = [1,2,3,4,5]
product = functools.reduce(lambda x, y: x * y, list_demo)
# print(product)