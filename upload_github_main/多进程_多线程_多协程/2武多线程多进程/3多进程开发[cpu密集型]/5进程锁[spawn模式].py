import multiprocessing
import time

def task(lock):
    print('开始')
    print(lock)
    with lock:
        pass
    print(lock)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    # 进锁
    lock = multiprocessing.RLock()
    lock.acquire()
    print(lock)
    for i in range(3):
        p = multiprocessing.Process(target=task,args=(lock,))
        p.start()
    # spawn模式下好像只能主进程等待子进程执行完毕后才有效
    # 但是我取消这个sleep的demo，也不报错。。
    time.sleep(10)