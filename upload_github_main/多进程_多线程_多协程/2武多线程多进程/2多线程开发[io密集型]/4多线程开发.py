import threading


loop = 1000000
number = 0

def _add(count):
    global number
    for i in range(count):
        number += 1

# 1-使用start()
# t = threading.Thread(target=_add,args=(loop,))
# t.start()
# print(number)

# 2-使用join()
t = threading.Thread(target=_add,args=(loop,))
t.start()
t.join() # 等待当前线程的任务执行完毕后再向下继续执行
print(number)