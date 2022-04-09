class School:
    def __init__(self,name,addr,type):
        self.name = name
        self.addr = addr
        self.type = type

    def __del__(self):
        print("对象被释放了！")

s = School("apeland","beijing","master")
print("ddd")
print("ddd")
print("ddd")
# del s
print("ddd")