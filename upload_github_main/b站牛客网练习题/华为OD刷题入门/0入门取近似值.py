import math
# print(math.ceil(4.1))
# print(math.ceil(4.6))
# print(math.ceil(-4.1))
# print(math.ceil(-4.6))
#
# print(math.floor(4.1))
# print(math.floor(4.6))
# print(math.floor(-4.1))
# print(math.floor(-4.6))
# print('-------------------------------')
# print(round(4.6))
# print(round(4.1))
# print(round(4.5))
# print(round(4.49))
import math
i = float(input())
decimal = i % 1
if decimal > 0.5:
    print(math.ceil(i))
else:
    print(math.floor(i))