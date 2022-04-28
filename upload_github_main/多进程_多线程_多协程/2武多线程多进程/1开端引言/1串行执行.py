import time
import threading
"""
https://www.bilibili.com/video/BV1Ev411G7i3?p=2&spm_id_from=pageDriver
我们得到的结果是不管是使用多线程还是多进程,
都可以加速下载url_list里面的地址时间
"""

url_list = [
    ("视频1", "url1"),
    ("视频2", "url2"),
    ("视频3", "url3")
]




for name, url in url_list:
    # 创建线程,让每个线程都去执行task函数(参数不同)
    print("%s,%s" % (name, url))
    print(time.time())
