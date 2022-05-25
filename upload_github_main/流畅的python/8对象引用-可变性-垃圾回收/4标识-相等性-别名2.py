"""
is比较的是对象的标识[id--相当于地址]
==比较的是对象中的数据

"""

charles = {'name':'Charles L. Dodgson', 'born':1832}
alex = {'name':'Charles L. Dodgson', 'bron':1832,'balance':950}
print(alex == charles)
print(alex is not charles)