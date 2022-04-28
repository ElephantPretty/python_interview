import asyncio

# 协程函数
async def func():
    print("快来快来")


# 协程对象
result = func()
#asyncio.run(result) py3.7
#事件循环来执行协程函数
loop = asyncio.get_event_loop()
loop.run_until_complete(result)
