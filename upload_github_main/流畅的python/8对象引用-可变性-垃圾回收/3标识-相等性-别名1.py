charles = {'name':'Charles L. Dodgson', 'born':1832}
lewis = charles
# is比较id是否相同
print(lewis is charles)
print(id(charles),id(lewis))
lewis['balance'] = 950
print(charles)

a = [1,2,3]
b = [1,2,3]
# ==比较内容
print(a == b)