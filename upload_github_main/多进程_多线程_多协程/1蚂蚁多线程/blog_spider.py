import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 20 + 1)
]


def craw(url):
    """
    生产者-生产结果是每个html
    :param url:
    :return:
    """
    r = requests.get(url)
    # print(r.text)
    # print(url, len(r.text))
    return r.text


def parse(html):
    """
    消费者，拿到生产者的生产结果(html)进行解析
    parse得到了html后进行解析
    :param html:
    :return:
    """
    # class = "post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]

# craws(urls[0])
# print(urls)


if __name__ == "__main__":
    for result in parse(craw(urls[2])):
        print(result)
