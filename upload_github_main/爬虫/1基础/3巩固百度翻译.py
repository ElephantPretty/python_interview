# 破解百度翻译
# post请求(携带了参数)
# 响应数据是一组json数据
import requests
import json
if __name__ == "__main__":
    # 1-指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2-进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }
    # 3-参数处理
    word = input('enter a word:')
    data = {
        'kw':word
    }
    # 4-请求发送
    response = requests.post(url=post_url,data=data)
    # 5-获取响应数据:json()方法返回的是obj[如果响应数据是json类型的,才可以使用json()]
    dict_obj = response.json()
    # 持久化存储
    fileName = word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    # print(json.dump(dict_obj))
    json.dump(dict_obj,fp=fp,ensure_ascii=False)
    print('over!!')
