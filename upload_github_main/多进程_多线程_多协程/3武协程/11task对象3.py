import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

task_list = [
    # asyncio.ensure_future(func()),
    # asyncio.ensure_future(func())
    # 写外面的话因为事件循环还没有创建，此时不能直接用ensure_future,
    # 但是可以使用协程函数生成的协程对象[写在外面这种情况不多见]
    func(),
    func()
]

loop = asyncio.get_event_loop()
done,pending = loop.run_until_complete(asyncio.wait(task_list))
print(pending)
print(type(pending))