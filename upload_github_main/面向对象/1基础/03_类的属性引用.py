class People:
    nationality = "CN"
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


p1 = People("Mjj", 21, "M")
p2 = People("Alex", 22, "M")
p3 = People("Jack", 23, "F")
# 类属性的两种方法调用
print(People.nationality)
print(p1.nationality)
# 实例属性调用
print(p1.name)
# 实例自己改了国籍，是否可以?
# 相当于给p1实例创建了一个新实例属性，加了nationality这个实例属性
# 而不是更改的的类属性
p1.nationality = "TW"
print(People.nationality)
print(p1.nationality) # p1的nationality--实例属性
