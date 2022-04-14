import asyncio
import aiohttp
import blog_spider
import time

semaphore = asyncio.Semaphore(10)

"""
https://zhuanlan.zhihu.com/p/104918655 知乎协程理论
对于IO密集型除了多线程,还可以使用协程，单线程里面实现并发，至尊循环！！！
总结
至此Python中的协程就介绍完毕了，
示例程序中都是以sleep代表异步IO的，
在实际项目中可以使用协程异步的读写网络、读写文件、渲染界面等，
而在等待协程完成的同时，CPU还可以进行其他的计算，协程的作用正在于此。
那么协程和多线程的差异在哪里呢？多线程的切换需要靠操作系统来完成，当线程越来越多时切换的成本会很高，
而协程是在一个线程内切换的，切换过程由我们自己控制，因此开销小很多，这就是协程和多线程的根本差异。

面试问到了协程，没答好，现在试试！--1-13
"""
async def async_craw(url):
    """
    协程就是在异步IO里面执行的这个函数
    这是先爬完10个后，在爬后面的10个
    """
    async with semaphore:
        print("craw url: ", url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                await asyncio.sleep(5)
                print(f"craw url:{url}, {len(result)}")


loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls]
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("use time seconds: ", end - start)