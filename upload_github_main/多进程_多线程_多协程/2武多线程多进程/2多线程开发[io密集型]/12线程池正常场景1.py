import time
from concurrent.futures import ThreadPoolExecutor


def task(video_url,num):
    print("开始执行任务",video_url)
    time.sleep(2)
    print(num)

# 这个线程池最多维护10个线程
pool = ThreadPoolExecutor(10)

url_list = ["1.www.{}.com".format(i) for i in range(20)]

for url in url_list:
    # 在线程池中提交一个任务，线程池中如果有空现场，则分配一个线程去执行
    # 执行完毕后再将线程交还给线程池，没有空线程，则等待
    # url和2是参数,submit(函数名,参数1,参数2...)
    pool.submit(task,url,2)

"""
1-线程池正常使用
2-等待线程池的任务执行完毕，主线程在继续执行
"""
print('执行中')
pool.shutdown(True) # 等待线程池中的任务执行完毕后，在继续执行
print('end')
