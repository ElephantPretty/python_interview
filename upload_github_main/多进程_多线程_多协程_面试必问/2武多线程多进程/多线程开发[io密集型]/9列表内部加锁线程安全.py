import threading

data_list = []

lock_object = threading.RLock()


def task():
    print("开始")
    for i in range(1000):
        # 列表的这些append和extend是线程安全的，都自动加了锁
        data_list.append(i)
    print(len(data_list))


for i in range(2):
    t = threading.Thread(target=task)
    t.start()