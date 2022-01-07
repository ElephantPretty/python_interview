import threading
import time

import blog_spider


def single_thread():
    print("single_thread begin")
    # 单线程
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single_thread end")


def multi_thread():
    print("multi_thread begin")
    threads = []
    for url in blog_spider.urls:
        # args传入的是一个元组
        # 爬虫这种类型属于IO密集型
        threads.append(threading.Thread(target=blog_spider.craw, args=(url,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        # join是等待时间
        thread.join()
    print("multi_thread end")


"""
多线程进行了技术优化，使爬虫变快了2倍，
爬虫不是重点，重点在于应用场景和思路
"""
if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print('single thread cost:', end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi thread cost", end - start, "seconds")

