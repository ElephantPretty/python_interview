from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print('draw circle')

class Rectangle(Shape):
    def draw(self):
        print('draw Rectangle')


class ShapeFactory(object):
    """
    工厂模式:暴露给用户去调用的
    用户可通过该类进行选择Shape的子类进行实例化
    """
    def create(self,shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Rectangle':
            return Rectangle()
        else:
            return None

fac = ShapeFactory()
obj = fac.create('Circle')
obj.draw()