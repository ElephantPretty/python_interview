# import threading
# num = 0
# lock_object = threading.Lock()
#
#
# def task():
#     print("开始")
#     # 第一个抵达的线程进入并上锁，其他线程就需要在此等待
#     lock_object.acquire()
#     lock_object.acquire()
#     global num
#     for i in range(100):
#         num += 1
#     lock_object.release()
#     lock_object.release()
#     print(num)
#
# """
# 这种情况程序会卡死,因为lock不支持嵌套锁
# """
# for i in range(2):
#     t = threading.Thread(target=task)
#     t.start()

import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

"""
各自拿着对方的锁不释放，而且想要获取对方的锁，
所以一直等待，出现了死锁现象
"""
def task():
    lock_1.acquire()
    time.sleep(1)
    lock_2.acquire()
    print(11)
    lock_2.release()
    print(111)
    lock_1.release()
    print(1111)

def task2():
    lock_2.acquire()
    time.sleep(1)
    lock_1.acquire()
    print(22)
    lock_1.release()
    print(222)
    lock_2.release()
    print(2222)

t1 = threading.Thread(target=task)
t1.start()

t2 = threading.Thread(target=task)
t2.start()