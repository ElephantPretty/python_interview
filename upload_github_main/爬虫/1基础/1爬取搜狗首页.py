import requests

if __name__ == '__main__':
    url = 'https://www.sogou.com'
    response = requests.get(url=url)
    # text字符串形式的响应数据
    page_text = response.text
    print(page_text)
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！！！')