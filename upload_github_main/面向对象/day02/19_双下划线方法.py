# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __len__(self):
#         print("trigger")
#         print(self.__dict__)
#         return 2
#
#     def __hash___(self):
#         print("hash...")
#
#     def __eq__(self,other):
#         print(self.name,other.name)
#
#
# p1 = Person("alex", 22)
# p2 = Person("Jack", 22)
# # print(len(p))
# # hash(p)
# # print(hash(p))
# print(p1 == p2)
class Brand():
    def __init__(self,name):
        self.name = name

    def __getitem__(self,item):
        print("---get item...", item)
        print(self.__dict__[item])
        print(self.__dict__)

    def __setitem__(self, key, value):
        print("set item")
        self.__dict__[key] = value

    def __delitem__(self,key):
        print("del...")

    def __delattr__(self,item):
        print("del obj.key时我执行")
        self.__dict__.pop(item)

b = Brand("小圆圈")
b["name"]
b["website"] = "www.apeland.cn"
b["website"] = "www.baidu.com"
print(b.website)
del b["name"]
del b.name
