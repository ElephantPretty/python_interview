from greenlet import greenlet
# https://www.bilibili.com/video/BV1NA411g7yf?p=3

def func1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()


def func2():
    print(3)
    gr1.switch()
    print(4)


gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch()