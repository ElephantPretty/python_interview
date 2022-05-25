import os

a = 2.2
print(type(a))
print(id(a))
a += 1
print(id(a))
a = range(1,10)
print(type(a))
print(list(a))
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
dic1 = {"name1":"张三1","name2":"张三2","name3":"张三3"}
# print(dic1)
# print(dic1.clear())
# print(dic1.pop("name1"))
# print(dic1.popitem())
del dic1["name2"]
print(dic1)
dic1 = {"name1":"张三","name2":"李四"}
dic2 = {"name3":"王五","name4":"赵六"}
zz = {**dic1,**dic2}
print(zz)

def fun1(*args,**kwargs):
    print(*args)
    print(**kwargs)


fun1(1,'yaozan','dba','hello')
def sum(*args):
    a = 0
    for n in args:
        a += n
    return a

print(sum(1,2,4,5))
tup = (1,2,3)
print(sum())

list1 = [63,34,25,12,22,11,90]
print(list1[0],list1[1])
for i in range(len(list1)):
    for j in range(0,len(list1) - i - 1):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)