# Your definition of the Vector class goes here. I have
# written the definition lines for you; replace the "pass"es
# with your code.

class Vector:

    def __init__(self, vx, vy):
        pass

    def __str__(self):
        pass

    def magnitude(self):
        pass

    def direction(self):
        pass
    
    def add(self, other):
        pass

    def scale(self, factor):
        pass


# Do not touch these lines; they will call the functions you have
# written to see if everything works correctly.

u = Vector(5, 2)
v = Vector(3, 4)
print('u is', u)
print('v is', v)
w = u.add(v)
print('w is', w)
s = u.scale(3)
print('scaled vector is', s)
