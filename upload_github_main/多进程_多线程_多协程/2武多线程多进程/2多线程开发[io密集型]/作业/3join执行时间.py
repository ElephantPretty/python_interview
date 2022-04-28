import threading
import time
"""
https://www.jianshu.com/p/81966695ddb7
"""
# 这个方法仅供内部使用
def _wait():
    time.sleep(6)

start_time = time.time()
t = threading.Thread(target=_wait)
t.start()
#
"""
1-当设置守护线程时，含义是主线程对于子线程等待timeout的时间将会杀死该子线程，
最后退出程序。所以说，如果有10个子线程，全部的等待时间就是每个timeout的累加和。
简单的来说，就是给每个子线程一个timeout的时间，让他去执行，时间一到，不管任务有没有完成，直接杀死。
2-没有设置守护线程时，主线程将会等待timeout的累加和这样的一段时间，时间一到，
主线程结束，但是并没有杀死子线程，子线程依然可以继续执行，直到子线程全部结束，
程序退出。
默认是非守护线程
"""
# 主线程等待子线程执行完毕后在往下走
t.join()
end_time = time.time()
print(end_time - start_time)