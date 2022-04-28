"""
题目6--比较水
定义一个函数，计算1-990的和，用for循环完成-490545
显然法二更好
"""
#法一
sum = 0
for i in range(1,991):
    # print(i)
    sum += i
# print(sum)

#法二
n = 990
def count(n, *args):
    sum = 0
    # *args用来将参数打包成tuple给函数体调用 这属于我个人的知识点，与本题关系不大
    # print(args)--('a', 'test') 类型是tuple
    for i in range(n + 1):# 默认从0开始
        print(i)
        sum += i
    print(sum)
count(n, 'a','test')