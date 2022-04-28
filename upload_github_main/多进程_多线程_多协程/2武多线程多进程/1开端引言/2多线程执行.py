import time
import requests
import threading
"""
def func(a1,a2,a3):
    pass
    
#　创建线程
t = thread.Thread(target=func,args=(11,22,33))
t.start()

"""

url_list = [
    ("视频1","url1"),
    ("视频2","url2"),
    ("视频3","url3")
]

def task(file_name, video_url):
    print("%s,%s"%(file_name,video_url))
    print(time.time())

print(time.time())
for name,url in url_list:
    # 创建线程,让每个线程都去执行task函数(参数不同)
    t = threading.Thread(target=task,args=(name,url))
    t.start()
# 不能在这里写print(time.time()),因为不会等待
