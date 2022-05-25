import weakref

s1 = {1,2,3}
print(id(s1))
s2 = s1
print(id(s2))
def bye():
    print('Gone with the wind')

ender = weakref.finalize(s1,bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)

def deractor(fun1):
    def func():
        print(1)
        fun1()
    return func
