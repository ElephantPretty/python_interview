class Bus:
    def __init__(self,passengers=None):
        if passengers is None:
            self.passergers = []
        else:
            self.passergers = list(passengers)

    def pick(self,name):
        self.passergers.append(name)

    def drop(self,name):
        self.passergers.remove(name)


import copy
bus1 = Bus(['Alice','Bill','Claire','David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1),id(bus2),id(bus3))
bus1.drop('Bill')
print(bus2.passergers)
print(id(bus1),id(bus2),id(bus3))
print(bus3.passergers)