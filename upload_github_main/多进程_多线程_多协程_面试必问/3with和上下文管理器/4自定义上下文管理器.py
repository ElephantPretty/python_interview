class File(object):
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename,self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()

# f = File() # 此时f指向的对象，就是一个上下文管理器
"""
1-先执行File("1.txt", "w")，会自动执行__init__(self,filename,mode)，自动调用__enter__方法，返回值给f
2-f.write("111")执行完毕后会自动调用__exit__

"""
with File("1.txt", "w") as f:
    f.write("111")

