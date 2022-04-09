class Dog(object):
    def sound(self):
        print('汪汪汪.....')

class Cat(object):
    def sound(self):
        print("喵喵喵.....")

def make_sound(animal_type):
    """
    统一调用接口--不常用
    """

    animal_type.sound()# 不管你传进来是什么动物，我都调用sound()方法


# dogObj = Dog()
# catObj = Cat()
# make_sound(dogObj)
# make_sound(catObj)

class Document:
    # 抽象类
    def __init__(self, name):
        self.name = name

    def show(self):
        # 异常处理
        raise NotImplementedError("Subclass must implement abstract method")


class Pdf(Document):
    # 子类重写
    def show(self):
        return 'Show pdf contents!'


class Word(Document):
    def show(self):
        return 'Show word contents!'

pdf_obj = Pdf('男模联系方式.pdf')
word_obj = Word('护士联系方式.word')
objs = [pdf_obj, word_obj]
for o in objs:
    print(o.show())