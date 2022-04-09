# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def fly(self):
#         print(self.name, "is flying...")
#
# s = Student("Jack")
# s.fly


class Flight(object):

    def __init__(self,name):
        self.flight_name = name

    def checking_status(self):
        print("connecting airline company api...")
        print("checking flight %s status" % self.flight_name)
        # 1 代表arrived 2 departed 3 canceled
        return 1

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("connot confirm the flight status..., please check later")

    # 语法要求，对静态属性进行修改
    @flight_status.setter
    def flight_status(self, status):
        print("chaning..flight status..",status)
        self.status = status

    # 静态属性删除
    @flight_status.deleter
    def flight_status(self):
        print("del...")



f = Flight("CA988")
f.flight_status
f.flight_status = 2
print(f.flight_status)
del f.flight_status
# f.flight_status = 1