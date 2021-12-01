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
    
    def reflect_x(self):
        ''' Reflect a point about the x-axis. '''
        return self.x, -self.y

    
# Determine a point and reflect it about the x-axis
p = Point(3, 5)
print(p.reflect_x())
