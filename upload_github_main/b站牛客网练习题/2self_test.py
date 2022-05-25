
# str2 = str1.split(',')
#
# str3 = str(str2[0]).split(' ')
# finish_str_1 = str3[1] + ' ' + str3[0]
# str4 = str(str2[1]).split(' ')
# finish_str_2 = str4[3] + ' ' + str4[2] + ' ' + str4[1]
# finish_str_3 = finish_str_1 + ', ' + finish_str_2
# str1=str1[::-1]
# 第一题结果
print(str1)
a = 'hello world, god bless you'
print(a[::-1])

"""
开辟一个新空间--再从最末尾开始填入
"""
# for i in range(1,len(str2[0])):
#     # print(i)
#     # print(len(str2[0]) - i)
#     print(str2[0][len(str2[0]) - i])
#     str3 += str2[0][len(str2[0]) - i]
# print(str3)

"""          
js函数--实现对一个数字每三位加一个逗号,比如100000
输入100,000--不考虑负数和小数
意思就是只考虑正数
"""
def js(num):
    """
    看起来像除法来解决
    每次除以10 如果能除以3次则加一个逗号
    1-首先要判断这个数字的位数
    2-根据位数来看加多少个逗号
    :param num:
    :return:
    """
    num_count = 0
    while(num%10):
        num_count += 1
        num /= 10
    print(num_count)
    # print(num)

# js(100000)