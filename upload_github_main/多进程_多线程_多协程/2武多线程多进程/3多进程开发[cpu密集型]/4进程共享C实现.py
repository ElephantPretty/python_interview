# python底层是c写的
"""
1-c语言来写[少]
2-manager【多】
3-队列,queue【多】
4-pipes[少]

"""
from multiprocessing import Process,Value,Array

def func(n, m1, m2):
    n.value = 888
    m1.value = 'a'.encode('utf-8')
    m2.value = '武'

if __name__ == '__main__':
    num = Value('i', 666)
    print(type(num))
    v1 = Value('c')
    v2 = Value('u')
    p = Process(target=func, args=(num,v1,v2))
    p.start()
    p.join()
    print(num.value)
    print(v1.value)
    print(v2.value)