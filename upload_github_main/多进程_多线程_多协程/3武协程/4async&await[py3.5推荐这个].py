# py3.4以上 asyncio
import asyncio

async def func1():
    print(1)
    # 网络IO请求：下载一张图片
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    # 网络IO请求：下载一张图片
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

"""
这个方式是遇到io阻塞自动切换，和前面两种方式不一样
"""
# 协程函数必须通过下面这种方式来执行
# 生成或获取一个事件循环[死循环]
loop = asyncio.get_event_loop()
# 将任务放到任务列表
loop.run_until_complete(asyncio.wait(tasks))