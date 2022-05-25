"""
https://www.bilibili.com/video/BV1r7411b7Uv?spm_id_from=333.337.search-card.all.click
字符串反转
逗号切割
切割的子单词作为单元反转
45结束--每题20分钟--19:31
hello world -> world hello
"""
# 输入
# list()
str1 = 'hello world, god bless you'
print(str1[::-1])
list_str1 = str1.split(',')
empty_str = ''
# for i in list_str1:
#     empty_str.join(i[::-1])
# print(empty_str)
# print(list_str1[::-1])
# print(' '.join(list_str1[::-1]))
# print(list_str1[::-1])
# list1=[1,2,3]
# list2=list(list1)
# print(id(list1),id(list2))

# s3="ilovechina"
# print("".join([i for i in reversed(s3)]))
# print(s3[::-1])
# s5 = "s".encode("gbk").decode(encoding="utf-8",errors="ignire")
# print(s5)
# a,b,c = map(int,input().split(' '))
# print(a,b,c)