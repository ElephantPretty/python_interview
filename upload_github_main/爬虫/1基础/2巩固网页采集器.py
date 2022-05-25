"""
爬虫巩固
1-爬取搜狗指定词条对应的搜索结果页面(简易网页采集器)
2-破解百度翻译
3-爬取豆瓣电影分类排行榜
4-爬取肯德基餐厅查询
5-爬取国家药品局
"""
import requests
# UA伪装--防反爬   UA检测--反爬策略
# UA伪装
# UA检测: User-Agent(请求载体的身份标识)
# 如果检测到请求的载体身份标识为某一款浏览器，
# 说明该请求是一个正常的请求。但是，如果检测到的请求的载体身份标识不是基于某一款浏览器的，
# 则表示该请求为不正常的请求(爬虫),则服务器端就很有可能拒绝该次请求
if __name__ == '__main__':
    url = 'https://www.sogou.com/web'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }
    #处理url携带的参数---封装到字典中
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    #对指定的url发起的请求对应的url是携带参数的,并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    fileName = kw + '.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)