def m3():
    with open("1.txt", "w") as f:
        f.write("python111")

"""
with关键字,open方法的返回值给变量f，
当离开with代码块的时候，系统自动调用f.close()方法
with作用和try/finally语句一样
with原理理解之前，需要先理解上下文管理器
"""
m3()