class Animal:
    species = 'animal'

    # write a class method show_species to print the species of the class
    # like this "It's dog". so that every subclass could call the same method
    # to print their own species
    # -- write your code here --
    @classmethod
    def show_species(cls):
        # print(cls.species)
        print("It's a %s!" % (cls.species))


# Make Class Dog inherit from Class Animal
# -- write your code here --
class Dog(Animal):
    species = 'dog'

    def __init__(self, breed):
        super().__init__()
        self.__breed = breed
        self.__color = "111"

    def barking(self):
        # print something like `Black Alaskan is barking!`
        # -- write your code here --
        print('%s %s is barking!' % (self.__color, self.__breed))

    # write a property function to return the color of the Dog that stores
    # at self.__color
    # -- write your code here --
    @property
    def get_color(self):
        return self.__color

    # write a setter function to change the dog's color which stores at
    # self.__color
    @get_color.setter
    def get_color(self, color):
        self.__color = color

    # -- write your code here --

a1 = Dog('小红')
a1.barking()
a1.get_color = 'red'
print(a1.get_color )
a1.barking()