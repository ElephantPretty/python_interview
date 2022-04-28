"""
背景：
令狐冲自小无父无母，
由师父华山派掌门“君子剑”岳不群和其妻师母宁中则扶养授武，情同亲生父母。
知识点：
单继承,
1-三种构造函数的区别：
2-新式类的写法：super(子类，self).__init__(参数1，参数2，....)
3-子类对父类方法的重写
"""

class Master(object):
    role = '华山派'

    def __init__(self,name):
        self.name = name
        print('练武之人的构造方法')

    def eat(self):
        print('%s正在吃东西'%(self.name))

class Apprentice1(Master):
    # 当子类不做初始化的时候，会自动继承父类的属性；我认为是相当于自动调用父类的构造方法
    print('子类创建成功')
    pass

class Apprentice2(Master):
    # 当子类做初始化（子类中包含新的属性）的时候，子类不会自动继承父类的属性；
    def __init__(self,age):
        self.age = age
        print('子类创建成功')

class Apprentice3(Master):
    # 当子类做初始化（子类中包含新的属性）的时候，如果子类调用super初始化了父类的构造函数，那么子类会继承父类的属性。
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
        print('子类创建成功')

    def eat(self):
        print('子类重写父类的eat方法')
        print('%s吃大瓜'%(self.name))

appre1 = Apprentice1('令狐冲1')
print(appre1.role)
print(appre1.name)
appre1.eat()
appre2 = Apprentice2(19)
print(appre2.age)
# name这个实例变量不能被调用
# print(appre2.name)
# eat 这个父类方法不能被调用
# print(appre2.eat())
# role这个类变量可以被调用
print(appre2.role)
appre3 = Apprentice3('令狐冲3',19)
print(appre3.age)
print(appre3.role)
appre3.eat()

