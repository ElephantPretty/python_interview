class Dog:
    # 狗的类属性有role
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
    # 人的类属性有role
    role = 'person'

    def __init__(self, name, sex, attack_val):
        self.name = name
        self.attack_val = attack_val
        self.life_val = 100
        self.sex = sex

    def attack(self, dog):
        # 人可以攻击狗，这里传递进来的dog也是一个对象
        # 人攻击狗，狗掉血
        dog.life_val -= self.attack_val
        print('人[%s]打了狗[%s],狗掉血[%s],还剩血量[%s]...'%(self.name,dog.name,self.attack_val,dog.life_val))


d1 = Dog("Mjj", "二哈", 30)
d2 = Dog("马金毛", "金毛", 40)
p1 = Person("Alex", "M", 50)
p1.attack(d1) # 两个对象交互
d1.bite(p1)
