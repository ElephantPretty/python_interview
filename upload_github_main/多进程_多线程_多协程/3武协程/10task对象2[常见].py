import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

async def main():
    print("返回值")
    # 创建task对象,将当前执行func函数任务添加到事件循环
    task_list = [
        asyncio.ensure_future(func()),
        asyncio.ensure_future(func())
    ]
    print("main结束")
    """
    当执行某协程遇到IO操作时,会自动切换执行其他任务
    此处的await是等待相对应的协程全都执行完毕并获取数据
    """
    # 相当于等待列表内的所有任务执行结束，timeout=None即全部执行完
    done,pending = await asyncio.wait(task_list,timeout=None)
    """
    done-执行完毕的结束结果集合
    pending-未执行完毕的
    """
    print(done, pending)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())