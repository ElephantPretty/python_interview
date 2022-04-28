# 读程序,请确认执行到最后的number是否一定为0
import threading
loop = int(1E7)
number = 0


def _add(loop=1):
    global number
    for _ in range(loop):
        number += 1


def _sub(loop=1):
    global number
    for _ in range(loop):
        number -= 1


number = 0
ta = threading.Thread(target=_add,args=(loop,))
ts = threading.Thread(target=_add,args=(loop,))
ta.start()
ts.start()
ta.join()
ts.join()
print(number)