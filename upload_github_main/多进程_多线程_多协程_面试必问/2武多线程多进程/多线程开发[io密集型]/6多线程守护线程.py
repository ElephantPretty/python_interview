import threading
import time

def task(arg):
    name = threading.current_thread().getName()
    print(name)
    time.sleep(5)
    print('任务')


t = threading.Thread(target=task,args=(11,))
"""
设置为非守护线程，主线程等待子线程，子线程执行完毕后，
主线程才结束（默认）
"""
# t.setDaemon(False)
# t.start()
# print('非守护线程,主线程会等待子线程执行完毕')

t.setDaemon(True)
t.start()
name = threading.current_thread().getName()
print(name)
print('守护线程,主线程不会等待子线程执行完毕，主线程执行完毕后程序结束')