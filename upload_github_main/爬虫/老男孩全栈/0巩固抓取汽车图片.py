import re
import uuid

import requests
from bs4 import BeautifulSoup

"""
总结
reponse = request.get('URL')
response.text http响应内容的字符串形式[请求url对应的页面内容]
response.content http响应内容的二进制(bytes)形式
response.encoding http header中猜测的响应内容编码方式
response.aparent_ecnoding 从内容分析出响应内容的编码方式(备选编码方式)
response.status_code 响应状态码

总结:
soup = beautifulsoup('<html>...</html>',features='html.parser')

find 返回找到的第一个标签
find_all 以list的形式返回找到的所有标签

v1 = soup.find('div') 找到第一个复合条件的--找soup孩子里面的第一个div
v1 = soup.find(id='i1') 找孩子里面第一个id='i1'的
v1 = soup.find('div', id='i1') 第一个idv并且id='i1'的标签

v2 = soup.find_all('div')
v2 = soup.find_all(id='i1')
v2 = soyp.find_all('div', id='i1')

obj = v1
obj = v2[0]

obj.text
obj.attrs
"""
response = requests.get(url='https://www.autohome.com.cn/wuhan/')
# print(response.headers['content-type'])
response.encoding = 'gb2312'
# print(response.)
# 得到一个 BeautifulSoup 的对象
soup = BeautifulSoup(response.text,features='html.parser')
target = soup.find(id='floornav-2')
target_list = target.find_all('li')
img_list = []
for i in target_list:
    a = i.find('a')
    if a:
        img = a.find('img')
        if img:
            img_url = img.attrs.get('data-src')
            if re.match('//',img_url):
                img_url = 'https:' + img_url
            img_list.append(img_url)
for img_url in img_list:
    img_res = requests.get(url=img_url)
    file_name = str(uuid.uuid1()) + '.jpg'
    with open(file_name,'wb') as f:
        f.write(img_res.content)
# for _ in img_list:
#     print(_)
# print(img_list)
# print(len(img_list))
    # if img:
    #
    #     img_url = 'https' + img_url
    #     print(img_url)

    # print(img_url)

    # if a:
    #     if a.find('img'):
    #         print(a.find('img'))
# print(target)
# print(response.status_code)
# print(response.apparent_encoding)
# print(response.content)
response = response.text
# print(response)