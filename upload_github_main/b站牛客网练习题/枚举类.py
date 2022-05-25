from enum import Enum
class Color(Enum):
    # 为序列值指定value
    red = 1
    green = 2
    blue = 3

print(Color.red)
print(Color['red'])
print(Color(1))

print(Color.red.value)
print(Color.red.name)
# print(Color(value.data))
# ClientTypeEnum(value.data)
for color in Color:
    print(color)