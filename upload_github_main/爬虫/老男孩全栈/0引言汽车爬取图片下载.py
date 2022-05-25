import requests
from bs4 import BeautifulSoup
response = requests.get(url='https://www.autohome.com.cn/news/')
# 字节
response.encoding = response.apparent_encoding
# 使用以下语法来把请求之后的响应传入解析器：
soup = BeautifulSoup(response.text, features='html.parser')
target = soup.find(id='auto-channel-lazyload-article')
# print(target)
# print(type(target))
li_list = target.find_all('li')
# print(li_list)
# print(type(li_list))
for i in li_list:
    a = i.find('a')
    # print(a)
    if a:
        # print(a.attrs.get('href'))
        txt = a.find('h3')
        # print(txt,type(txt))
        img_url = a.find('img').attrs.get('src')
        import re
        """
        //www2.autoimg.cn/soudfs/g30/M01/59/AD/120x90_0_autohomecar__ChxknGKBwvaAfd_7AABRZlXgb2U779.jpg
        https://www3.autoimg.cn/cubetopic/g28/M00/BE/FF/120x90_0_autohomecar__ChwFkmKBuu-AMO30AACuw7Nr7fU180.jpg
        """
        import re
        if re.match('//', img_url):
            img_url = 'https:' + img_url
        # print(img_url)
        img_response = requests.get(url=img_url)
        import uuid
        file_name = str(uuid.uuid4()) + '.jpg'

        with open(file_name, 'wb') as f:
            f.write(img_response.content)
"""
总结
reponse = request.get('URL')
response.text
response.content
response.encoding
response.aparent_ecnoding
response.status_code

总结:
soup = beautifulsoup('<html>...</html>',features='html.parser')
soup.find('div') 孩子里面第一个等于div的
soup.find(id='i1')
soup.find('div', id='i1')

soup.find_all('div')
soup.find_all(id='i1')
soyp.find_all('div', id='i1')

obj = v1
obj = v2[0]

obj.text
boj.attrs
"""