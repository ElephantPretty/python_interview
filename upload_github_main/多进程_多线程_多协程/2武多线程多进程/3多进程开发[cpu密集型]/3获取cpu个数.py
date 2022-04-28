import multiprocessing


def task():
    pass


# 意思是可以创建4个进程，
if __name__ == '__main__':
    print(multiprocessing.cpu_count())
    for i in range(multiprocessing.cpu_count() - 1):
        p = multiprocessing.Process(target=task)
        p.start()
