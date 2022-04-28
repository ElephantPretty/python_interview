class School:
    def __init__(self,name,addr,type):
        self.name = name
        self.addr = addr
        self.type = type

    def __call__(self,*args,**kwargs):
        print(self,args,kwargs)

s = School("apeland","beijing","master")
s() # 实例名()就执行
School('1','2','3')()