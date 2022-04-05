class Dog:
    # 属性，类属性，类变量
    # 公共属性
    d_type = "京巴"
    # 属性, 类属性，类变量
    sss = "sss"
    def __init__(self, name, age):
        # 初始化方法-构造方法-构造函数
        # 实例化会自动执行，进行一些初始化工作
        print('hahahaha', name, age)
        # name age相当于实例的私有变量
        # 若要name age这两个值真正存到实例里面，需要把2个值存到实例里面
        self.name = name # 绑定参数值到实例2
        self.age = age

    def say_hi(self):
        # self代表实例本身!!
        # 第一个参数，必须是self[可以是别的名称],self代表实例本身
        print("hello, i am a dog, my type is ", self.d_type, self.name, self.age)

# 实例化
d1 = Dog('金毛',1)
d2 = Dog('柯基',2)

d1.say_hi() #调用方法，实例．方法--其实自动是d2.say_hi(d2)
# print(d2)
d2.say_hi()

# print(d1.d_type) # 实例.属性
# print(id(d1.d_type), id(d2.d_type))
#　两种调用方法－－类属性
print(Dog.d_type)
print(d1.d_type)
# 实例属性--只能通过实例来调用，实例只存在自己的实例内存里面
print(d1.name)