"""
最终获取同意结果
"""
import time
import random
from concurrent.futures import ThreadPoolExecutor, Future


def task(video_url):
    print("开始执行任务", video_url)
    time.sleep(2)
    return random.randint(0, 10)


# 　创建线程池，最多维护１０个线程
pool = ThreadPoolExecutor(10)
future_list = []
url_list = ["www.xxx-{}.dom".format(i) for i in range(5)]
for url in url_list:
    """
    在线程池中提交一个任务，线程池中如果有空闲线程，
    则分配一个线程去执行

    """
    future = pool.submit(task, url)
    """
    1-同步：一定要等任务执行完了，得到结果，才执行下一个任务。 异步：不等任务执行完，直接执行下一个任务
    2-程序将 task 函数提交（submit）给线程池后，submit 方法会返回一个 Future 对象，
    Future 类主要用于获取线程任务函数的返回值。由于线程任务会在新线程中以异步方式执行，
    因此，线程执行的函数相当于一个“将来完成”的任务，所以 Python 使用 Future 来代表。
    3-add_done_callback(fn)：为该 Future 代表的线程任务注册一个“回调函数”，
    当该任务成功完成时，程序会自动触发该 fn 函数。
    """
    """
    比如task是专门下载,done是将下载的文件持久化
    """
    future_list.append(future)

pool.shutdown(True)
for fu in future_list:
    print(fu.result)

