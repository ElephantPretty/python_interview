"""
py2只有进程池
py3添加了线程池，并且线程池和进程池移到了concurrent[推荐]
但是multiprocess里面也有进程池[不推荐用这个]
"""

import time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

def task(num):
    print("执行",num)

if __name__ == '__main__':
    pool = ProcessPoolExecutor(3)
    for i in range(10):
        # 等待是在进程池内部执行的,不会在这里等待[如果没有空余进程来执行任务]
        pool.submit(task, i)
    print(1)
    print(2)
