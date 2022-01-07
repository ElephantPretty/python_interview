"""
题目5
打印0-10之间的奇数
下面两个等价
"""

for i in range(0,11):
    if i % 2 != 0:
        print("奇数", i , " ")

for i in range(11): #默认是从 0 开始。例如range（11）等价于range（0， 11）;
    if i % 2 != 0:
        print("奇数", i, " ")