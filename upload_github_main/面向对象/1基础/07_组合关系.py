# 由一堆组件构成一个完整的实体，组件本身独立，但又不能自己运行，必须和宿主组合在一起，运行
class Dog:
    role = 'dog'

    def __init__(self, name, breed, attack_val):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100

    def bite(self, person):
        # 狗可以咬人，这里传递进来的person也是一个对象
        person.life_val -= self.attack_val
        print("狗[%s]咬了人[%s],人掉血[%s],还剩血量[%s]..."%(self.name,person.name,self.attack_val,person.life_val))

class Person:
    role = 'person'

    def __init__(self, name, sex, attack_val):
        self.name = name
        self.attack_val = attack_val
        self.life_val = 100
        self.sex = sex
        self.weapon = Weapon()

    # def attack(self, dog):
    #     # 人可以攻击狗，这里传递进来的dog也是一个对象
    #     # 人攻击狗，狗掉血
    #     dog.life_val -= self.attack_val
    #     print('人[%s]打了狗[%s],狗掉血[%s],还剩血量[%s]...'%(self.name,dog.name,self.attack_val,dog.life_val))

# 一个组件
class Weapon:
    def dog_stick(self, obj):
        """打狗棒"""
        self.name = "打狗棒"
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def knife(self,obj):
        self.name = "屠龙刀"
        self.attack_val = 80
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def gun(self,obj):
        self.name = "AK47"
        self.attack_val = 100
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        print("[%s]被[%s]攻击了，掉血[%s],还剩血量[%s]..."%(obj.name,self.name,self.attack_val,obj.life_val))

d1 = Dog("恶犬", "二哈", 30)
p1 = Person("洪七公", "M", 50)
d1.bite(p1)
p1.weapon.gun(d1)
