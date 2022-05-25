import re
"""
re.match（）的概念是从头匹配一个符合规则的字符串
re.search（）函数会在字符串内查找模式匹配,
只要找到第一个匹配然后返回，如果字符串没有匹配，则返回None

"""
result = re.match("hello", "hello, world")
if result:
    print(result.group())
else:
    print("匹配失败！")

result1 = re.search(r"\d+", "阅读次数为 9999")
print(result1.group())
