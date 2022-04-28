# py3.4以上 asyncio
import asyncio

# 加上这个装饰器之后--变为协程函数
@asyncio.coroutine
def func1():
    print(1)
    # 网络IO请求：下载一张图片
    yield from asyncio.sleep(2)
    print(2)


@asyncio.coroutine
def func2():
    print(3)
    # 网络IO请求：下载一张图片
    yield from asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

"""
这个方式是遇到io阻塞自动切换，和前面两种方式不一样
"""
# 协程函数必须通过下面这种方式来执行
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))