"""

浅拷贝之所以称为浅拷贝，是它仅仅只拷贝了一层，拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已
浅拷贝第二层面对不可变对象[数值int,float,字符串,元组]会友好一点
面对可变对象[list,dict,set]会达不到我们预期的效果
"""
l1 = [3,[66,55,44],(7,8,9)]
# print(id(l1))
l2 = list(l1)
l1.append(100)
# print(id(l1))
l1[1].remove(55)
print('l1:',l1)
print('l2:',l2)
l2[1] += [33,22]
l2[2] += (10,11)
print('l1:',l1)
print('l2:',l2)

# 元组属于不可变对象,假如值改变,地址也会发生变化
set1 = (1,2)
print(id(set1))
set1 += (1,2)
print(set1)
print(id(set1))
# 集合set属于属于可变对象--值改变,地址不变
s = set()
s = {1,2,3,4}
print(s)
print(id(s))
s.add(5)
print(s)
print(id(s))
