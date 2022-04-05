class Animal:
    a_type = "哺乳动物"

    def __init__(self,name,age,sex):
        print("父类的构造方法")
        self.name = name
        self.age = age
        self.sex = sex


    def eat(self):
        print("%s is eating...."%self.name)


class Person(Animal):
    a_type = "哺乳高等动物"

    def __init__(self, name, age, sex, hobbie):
        # python2常用
        # Animal.__init__(self, name, age, sex)
        # python3--和上面一样
        # super(Person,self).__init__(name, age, sex)
        # python3--一样
        super().__init__(name, age, sex)
        print("子类的构造方法")
        self.hobbie = hobbie



    def talk(self):
        print("person %s is talking..."%self.name)

    def eat(self):
        # 执行了父类的方法--不完全重构
        # python2
        # Animal.eat(self)
        # python3--执行父类方法
        super().eat()
        print("人在优雅的吃...")


def Dog(Animal):
    def chase_rabbit(self):
        print("狗在追逐兔子。。。")


# p = Person("Alex", 22, "M")
# p.eat()
# p.talk()
# print(p.a_type)
p = Person("Alex", 22, "M", "赚钱")
p.eat()
p.talk()
print(p.a_type)
print(p.hobbie)