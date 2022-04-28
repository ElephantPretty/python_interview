def m2():
    f = open("1.txt","w")
    try:
        f.write("python111")
    except IOError:
        print("oops error")
    finally:
        f.close()

"""
通过异常处理，可以规避资源写入错误时，资源可能不会释放的问题
"""
m2()