class Person(object):
    def __init__(self,name,age):
        # 实例变量-成员变量-
        self.name = name
        self.age = age
        # 私有变量-私有属性
        self.__life_val = 100

    def get_life_val(self):
        # 这样外面是修改不了这个属性的
        print("生命值还有",self.__life_val)
        return self.__life_val

    def got_attack(self):
        self.__life_val -= 20
        print("被攻击了,生命值减20")
        self.__breath()
        return self.__life_val
    # 私有方法
    def __breath(self):
        print("%s is breathing..."%self.name)


a = Person("Alex", 22)
# a.life_val -= 50
a.get_life_val()
a.got_attack()
# a.__breath() 私有方法从外部无法直接访问
# 实例名._类名+方法名()--一般不这么用
a._Person__breath()
# 修改私有数据
a._Person__life_val = 10
a.get_life_val()
#　实例生成后，再创建的私有属性，并不具有私有性，是可以直接访问的
a.__val = 444
print(a.__val)