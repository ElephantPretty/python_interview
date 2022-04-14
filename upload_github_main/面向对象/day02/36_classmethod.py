"""
@classmethod
类方法只能访问类变量，不能访问实例变量, 也就是跟类有关，跟实例无关。
类方法当然只能访问类变量拉！！！cls
cls隐式传入当前类
"""

class ParentClass(object):
    var = "test for parent"
    @classmethod
    def clasmethod(cls):
        print(cls.var)

class SubClass(ParentClass):
    var = "test for sub"
    """
    子类默认调用父类的构造方法
    相当于
    def __init__(self):
        super().__init__()
        
        当SubClass.clasmethod()时
        super().__init__()传入了当SubClass这个类
        所以父类clasmethod(cls)里面的cls变为了SubClass这个类，
        即输出test for sub
    """

ParentClass.clasmethod()
SubClass.clasmethod()