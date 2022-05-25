a = [10,20]
b = [a, 30]
a.append(b)
print(a)
from copy import deepcopy
c = deepcopy(a)
print(c)