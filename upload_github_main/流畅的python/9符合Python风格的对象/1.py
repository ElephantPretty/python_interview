class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))


v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x, y = v1
print(x, y)

print(v1)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
