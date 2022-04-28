class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print("walking...")

def talk(self):
    print(self.name, "is speaking")


# 反射可以通过字符串的形式来操作一个对象的属性
p = Person("Alex", 22)
if hasattr(p,"name"):
    print("111111")

"""
getattr()
hasattr()
setattr()
delattr()

hasattr(object,'attrName')：判断该对象是否有指定名字的属性或方法，返回值是bool类型
setattr(object,'attrName',value)：给指定的对象添加属性以及属性值
getattr(object,'attrName')：获取对象指定名称的属性或方法，返回值是str类型
delattr(object,'attrName')：删除对象指定名称的属性或方法值，无返回值
"""
a = getattr(p, "age")
print(a)
# hasattr
# user_command = input(">>:").strip()
# if hasattr(p,user_command):
#     func = getattr(p,user_command)
#     # walk
#     print(func)
#     func()
# setattr() 赋值
# 设置了一个静态属性 static
setattr(p,"sex","Female")
print(p.sex)
# 实例+方法
# setattr(p,"speak",talk)
# p.speak(p)
# 对类加方法
# setattr(Person,"speak2",talk)
# p.speak2()
# del p.age 和delattr(p,"age" )区别不大
delattr(p,"age")
# p.age
"""
__main__就代表模块本身,self
"""
# if __name__ == "__main__":
#     # 只会在被别的模块导入的时候发挥作用
#     print("hahahaha")
# import sys
# print(sys.modules["__main__"])
# mod = sys.modules[__name__]
# if hasattr(mod,"p"):
#     o = getattr(mod, "p")
#     print(o)
# print(p)

class User:
    def log(self):
        print('欢迎来到登录页面')
    def register(self):
        print('欢迎来到注册页面')
    def save(self):
        print('欢迎来到存储页面')

u = User()
while True:
    user_cmd = input(">>:").strip()
    if hasattr(u, user_cmd):
        func = getattr(u,user_cmd)
        func()