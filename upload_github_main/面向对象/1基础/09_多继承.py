class Base(object):
    def fight(self):
        print("动物在打架....")

class ShenXianBase(Base):
    def fight(self):
        print("神仙始祖们在天地边界打架。。。。")


class ShenXian(ShenXianBase):
    """神仙类"""
    def fly(self):
        print("神仙都会飞")

    def fight(self):
        print("神仙在打架")

class MonkeyBase(Base):
    pass
    # def fight(self):
    #     print("猿猴在打架")


class Monkey(MonkeyBase):
    def eat_peach(self):
        print("猴子都喜欢吃桃子...")

    # def fight(self):
    #     print("猴子在打架")


class MonkeyKing(Monkey,ShenXian):
    """
    多继承是有顺序的,从左到右继承

    """
    def play_goden_stick(self):
        print("孙悟空玩金箍棒")



m = MonkeyKing()
m.fly()
m.eat_peach()
m.play_goden_stick()
m.fight()