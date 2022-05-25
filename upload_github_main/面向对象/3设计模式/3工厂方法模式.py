from abc import abstractmethod, ABCMeta


class ShapeFactory(object):
    # 工厂类
    def getShape(self):
        return self.shape_name


class Circle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Circle"

    def draw(self):
        print('draw circle')


class Rectangle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Retangle"

    def draw(self):
        print('draw Rectangle')


class ShapeInterfaceFactory(metaclass=ABCMeta):
    """接口基类"""
    @abstractmethod
    def create(self):
        # 把要创建的工厂对象装配进来
        pass


class ShapeCircle(ShapeInterfaceFactory):
    def create(self):
        return Circle()

class ShapeRectangle(ShapeInterfaceFactory):
    def create(self):
        return Rectangle()

shape_interface = ShapeCircle()
obj = shape_interface.create()
print(obj.getShape())
print(obj.draw())


shape_interface2 = ShapeRectangle()
obj2 = shape_interface2.create()
obj2.draw()





