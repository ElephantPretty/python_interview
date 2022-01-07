"""
题目7-初看感觉意义不大。。。------后面感觉对于科学理论的建立，我认为是有帮助的
对于函数来说,return是什么？
1、return是一个函数结束的标志，函数内可以有多个return,但只要执行一次，整个函数就会结束运行，默认 return None *****
2、return的返回值无类型限制，即可以是任意数据类型 *****
3、return的返回值无个数限制，即可以逗号分割开多个任意类型的值 *****
    0个：返回None,ps:不写return默认会在函数的最后一行添加return None
    1个:返回的值就是该值本身
    多个:返回值是元组
4、return关键字：return是函数结束的表示,****,
那么利用这一点就可以结束循环(循环在函数里面可以利用这一点结束)
"""
# 什么是函数值？
# l = [1, 2, 3, 4]
# print(id(l))
# n = l.pop(0)
# print(l)
# print(id(l))

# def factory(a):
#     print('正在制造手机')
#     if a == 1:
#         return 'aaaa'
#     else:
#         print('测试')
#     #(True, [1, 2, 3, 4])--多个就放在元组里面
#     return True,[1,2,3,4]
#     print('测试1')
#     return 2
#
#
# b = factory(2)
# # 假若函数里面没有return 则返回None
# print(b)

a = 1
def factory(a):
    print('正在制造手机')
    while True:
        while 1:
            if a == 3:
                return
            else:
                a += 1
            print(a)

factory(a)