import queue
import threading

import blog_spider
import time
import random


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url) # 生产者抓到html后存入html队列
        html_queue.put(html)
        print(threading.current_thread().name, f"craw {url}",
              "url_queue.size=", url_queue.qsize()
              )
        time.sleep(random.randint(1,2))#随机睡1-2s


def do_parse(html_queue: queue.Queue, fout):
    while True:
        # 消费者从html队列中取出结果，来进行消费（抓取html中的文章标题）
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name, f"result.size", len(result),
              "html_queue.size=", html_queue.qsize())
        time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)
    # 3个生产者线程
    for idx in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue),
                             name=f"craw{idx}")
        t.start()
    fout = open("02.data.txt", "w")
    # 2个消费者线程
    for idx in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout),
                             name=f"craw{idx}")
        t.start()





