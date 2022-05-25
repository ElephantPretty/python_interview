"""
https://blog.csdn.net/win_turn/article/details/52998912
格式: str[begin:end:step]
字符串截取遵循“左闭右开”原则，也叫“包左不包右”
str,字符串.
begin,起始位置.
end,结束位置.
step,间隔.s不等于0.默认为1
注:
区间为左闭右开.
step>0,表示从左往右.
step<0,表示从右往左.
"""
spam = 'abcdefghijklmn'
# 0到13
#-14到-1
# bcdefg
# print(spam[1:7:1])
# abcdefghijklmn->acegikm
# print(spam[:13:2])
# ghijk
# print(spam[-8:11:1])
# print(spam[0])
# print(spam[4])
# print(spam[-1])
# print(spam[0:5])
# print(spam[:5])
# print(spam[6:])
# print(','.join(['cat','rats','bats']))
# print(' '.join(['My', 'name', 'is', 'Simon']))
# print('ABC'.join(['My','name','is','Simon']))
# print('AA BB CC DD'.split(' '))
# 取后3位--中软第一面题目 左闭右开最关键！！！！！！！！！！！
# print(spam[-3:])
# print(spam[-3:]) # print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
# print(spam[-1:-11])

# 面试题1：如何反转一个字符串
s1 = 'abcde'
s2 = ''
for i in s1:
    s2 = i + s2
print(s2)
# 面试题2：如何用分片反转字符串
print(s1[-1:-5])
print(s1[::-1])