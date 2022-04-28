import asyncio

async def func():
    print("1111")
    # 事件循环遇到这个时会切换到其他任务进行执行[不会继续往下执行],直到这个结束
    response = await asyncio.sleep(2)
    print("结束",response)

result = func()
loop = asyncio.get_event_loop()
loop.run_until_complete(result)
