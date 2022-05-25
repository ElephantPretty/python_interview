# 4 .实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn ）。
def self_pow_function(x, n):
    tempary = x
    if n == 0:
        return 1
    for i in range(n - 1):
        # print(i)
        x = x * tempary
        # print(x)
    return x

print(self_pow_function(2,0))
print(self_pow_function(2,3))
print(self_pow_function(2,1))
print(self_pow_function(0,2))
# print(pow(2,0))
# print(pow(2,3))
# print(pow(2,1))
# print(pow(0,2))