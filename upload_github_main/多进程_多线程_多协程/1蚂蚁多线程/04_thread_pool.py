import concurrent.futures
import blog_spider


with concurrent.futures.ThreadPoolExecutor() as pool:
    """
    craw
    """
    # 推荐使用map，map必须先准备好数据---使用线程时优先推荐使用线程池
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    # zip是打包成元组
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over ")


with concurrent.futures.ThreadPoolExecutor() as pool:
    """
    parse
    """
    futures = {}
    for url, html in htmls:
        #返回一个future对象，单个提交
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url
    #顺序一定
    # for future, url in futures.items():
    #     print(url, future.result())
    # 顺序不定-哪个任务先执行完成，就优先执行
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())