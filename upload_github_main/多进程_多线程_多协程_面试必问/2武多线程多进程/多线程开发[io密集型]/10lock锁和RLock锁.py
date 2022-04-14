import threading
import time

lock_object = threading.RLock()
lock_object1 = threading.Lock()
"""
Rlock支持嵌套锁
lock不支持嵌套所
开发种RLock更实用
单独开关锁【不嵌套】，lock效率更高

"""
# def task():
#     print("开始")
#     lock_object.acquire()
#     lock_object.acquire()
#     print(123)
#     lock_object.release()
#     lock_object.release()

def task():
    # 会出现死锁现象，因为lock不支持嵌套锁
    print("开始")
    lock_object1.acquire()
    lock_object1.acquire()
    print(123)
    lock_object1.release()
    lock_object1.release()


for i in range(3):
    t = threading.Thread(target=task)
    t.start()