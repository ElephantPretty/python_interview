import threading
import time
"""
https://www.jianshu.com/p/81966695ddb7
"""
# 这个方法仅供内部使用
def _wait():
    time.sleep(60)

start_time = time.time()
t = threading.Thread(target=_wait)
# 非守护模式,主线程就算执行完毕,也需要等待子线程执行完成后方可结束程序
t.setDaemon(False)
t.start()
end_time = time.time()
print(end_time - start_time)