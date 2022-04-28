class Student(object):
    role = "Stu"

    def __init__(self,name):
        self.name = name

    @staticmethod
    def fly(self):
        print(self.name, "is flying...")

    @staticmethod
    def walk(self):
        print("student walking...")

s = Student('Jack')
s.fly(s)
s.walk(s)