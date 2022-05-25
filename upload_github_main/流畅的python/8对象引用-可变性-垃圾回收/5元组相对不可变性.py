t1 = (1,2,[30,40])
t2 = (1,2,[30,40])
#比较内容
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2)
