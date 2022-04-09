class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("Alex",22)
# print(type(p))
# print(type(Person))
def __init__(self,name,age):
    self.name = name
    self.age = age

dog_class = type("Dog",(object,),{"role":"dog","__init__":__init__})
print(dog_class)
d = dog_class("Mjj",22)
print(d.role)
print(dir(dog_class))