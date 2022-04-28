import threading

lock_object = threading.RLock()
loop = 100000
number = 0
"""
两个线程必须要放同一把锁
"""

# def _add(count):
#     lock_object.acquire()
#     global number
#     for i in range(count):
#         number += 1
#     lock_object.release()
#
#
# def _sub(count):
#     lock_object.acquire()
#     global number
#     for i in range(count):
#         number -= 1
#     lock_object.release()
#
#
# t1 = threading.Thread(target=_add, args=(loop,))
# t2 = threading.Thread(target=_sub, args=(loop,))
# t1.start()
# t2.start()
# t1.join() # t1线程执行完毕后，主线程才继续往后走
# t2.join() # t2线程执行完毕后，主线程才继续往后走
# print(number)

def task():
    print("开始")
    with lock_object:
        # 上下文管理器来解决锁自动使用和释放问题
        global number
        for i in range(1000):
            number += 1
    print(number)

for i in range(2):
    t = threading.Thread(target=task)
    t.start()