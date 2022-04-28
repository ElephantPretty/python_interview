import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

async def main():
    print("返回值")
    # 创建task对象,将当前执行func函数任务添加到事件循环
    task1 = asyncio.ensure_future(func())
    task2 = asyncio.ensure_future(func())
    print("main结束")
    """
    当执行某协程遇到IO操作时,会自动切换执行其他任务
    此处的await是等待相对应的协程全都执行完毕并获取数据
    """
    result1 = await task1
    result2 = await task2
    print(result1, result2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())