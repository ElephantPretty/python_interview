import time
import multiprocessing

"""
进程创建之后，在进程中还会创建一个线程
t = mutiprocessing.Process(target=函数名,args=(name,url))
t.start()
"""

url_list = [
    ("视频1", "url1"),
    ("视频2", "url2"),
    ("视频3", "url3")
]


def task(file_name, video_url):
    print("%s,%s" % (file_name, video_url))
    print(time.time())


if __name__ == "__main__":
    """
    linux-fork
    win:spawn
    max:fork和spam[py3.8默认设置spawn]
    spawn要求使用多进程时代码放到__name__里面    
    """
    print(time.time())
    for name, url in url_list:
        t = multiprocessing.Process(target=task, args=(name, url))
        t.start()
