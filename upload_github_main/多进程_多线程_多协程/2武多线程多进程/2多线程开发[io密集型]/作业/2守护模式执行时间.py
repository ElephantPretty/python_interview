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
# 守护模式,主线程执行完毕后,程序结束[不管子线程是否执行完毕]
t.setDaemon(True)
t.start()
end_time = time.time()
print(end_time - start_time)