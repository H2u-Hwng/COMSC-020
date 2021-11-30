class Point:
    ''' Point class for representing and manipulating x,y coordinates. '''

    def __init__(self, initX, initY):
        ''' Create a new point at the given coordinates. '''
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def slope_from_origin(self):
        # Check whether the denominator is 0
        if self.x == 0:
            slope = 'None'
        else:
            slope = self.y / self.x
            
        return slope


# Determine point 1 and display its slope from origin
p1 = Point(4, 10)
print(p1.slope_from_origin())

# Determine point 2 and display its slope from origin
p2 = Point(0, 10)
print(p2.slope_from_origin())
