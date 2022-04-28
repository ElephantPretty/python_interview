# https://www.bilibili.com/video/BV1t34y197tv?p=9&spm_id_from=pageDriver
class RelationShip:
    """保存couple之间的对象关系"""
    def __init__(self):
        self.couple = []

    def make_couple(self, obj1, obj2):
        # 两个人就成了对象
        self.couple = [obj1, obj2]
        print("[%s]和[%s]确定了男女关系..."%(obj1.name, obj2.name))

    def get_my_parter(self, obj):
        # 这个self是RelationShip的实例
        print("找[%s]的对象"%obj.name)
        for i in self.couple:
            if i != obj: # 代表这个是obj的对象
                return i
        else:
            # 迭代完并且无break时会执行else里面的内容，python-for-else用法
            print("目前是空列表，没有对象")

    def break_up(self):
        print("[%s]和[%s]正式分手了...江湖再见..."%(self.couple[0].name,self.couple[1].name))
        self.couple.clear() # 分手


class Person:
    def __init__(self, name, age, sex, relation):
        self.name = name
        self.age = age
        self.sex = sex
        # 每个人的实例存储 关系对象
        self.relation = relation
        # 应该是一个对象，代表另一半
        # self.parter = None

    def do_private_stuff(self):
        pass

relation_obj = RelationShip()
p1 = Person("杨过",17,"M",relation_obj)
p2 = Person("小龙女",25, "F",relation_obj)
relation_obj.make_couple(p1, p2) # 2人成为对象
print(p1.relation.couple) # 这样可以通过p1直接找到p2[以relation作为中介]
print(p1.relation.get_my_parter(p1).name)
p1.relation.break_up()
p2.relation.get_my_parter(p2)






# # 双向绑定，关联
# p1.parter = p2 # 这样杨过的另一半就是小龙女
# p2.parter = p1 # 小龙女的另一半是杨过
# print(p1.parter.name,p2.parter.name)
# # 小龙女对杨过分手
# p2.parter = None
# # 杨过对小龙女分手
# p1.parter = None
# print(p1.parter)