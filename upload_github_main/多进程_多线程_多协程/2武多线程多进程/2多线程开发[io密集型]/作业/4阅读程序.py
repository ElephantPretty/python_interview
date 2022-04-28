# 读程序,请确认执行到最后的number是否一定为0
import threading
# 科学计数法-1乘以10的7次方
loop = int(1E7)


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
ts = threading.Thread(target=_sub,args=(loop,))
ta.start()
ta.join()
ts.start()
ts.join()
print(number)