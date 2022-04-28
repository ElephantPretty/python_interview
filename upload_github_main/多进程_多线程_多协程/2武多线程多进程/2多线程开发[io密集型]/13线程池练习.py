import threading
from concurrent.futures import ThreadPoolExecutor,Future


def task1():
    print("%s执行下载任务1"%(threading.current_thread().getName()))
    

def task2(future):
    print(future.result)
    print("%s执行下载任务1写入本地" % (threading.current_thread().getName()))


pool = ThreadPoolExecutor(10)
for i in range(10):
    future = pool.submit(task1)
    future.add_done_callback(task2)

pool.shutdown(True)
print("%s任务结束" % (threading.current_thread().getName()))