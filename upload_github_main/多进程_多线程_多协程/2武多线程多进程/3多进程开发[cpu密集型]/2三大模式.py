"""
win演示不了fork
https://www.bilibili.com/video/BV1Ev411G7i3?p=13
三大进程模式底层不好理解--需要多加练习

1-fork模式下紫禁城几乎拷贝父进程的所有资源[unix]，资源内存地址不一样
2-spawn模式下需要手动传父进程的资源才可以资源[unix,linux],这些资源是两份数据，内存地址不一样
3-forkserver也是手动传部分资源[部分linux]
创建子进程时会复制一个模板的内容
"""

import multiprocessing

def task(name):
    print(name)

if __name__ == '__main__':
    # multiprocessing.set_start_method("spawn")
    # name = []
    # p1 = multiprocessing.Process(target=task,args=(name,))
    # p1.start()
    multiprocessing.set_start_method("forkserver")
    name = []
    p1 = multiprocessing.Process(target=task,args=(name,))
    p1.start()