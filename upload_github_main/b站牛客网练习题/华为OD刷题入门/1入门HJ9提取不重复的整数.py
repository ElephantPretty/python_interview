number = '98876673'
number = number[::-1]
list = []
empty=""
for str in number:
    if str not in list:
        empty = empty + str
        list.append(str)
print(empty)