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

    def distanceFromPoint(self, otherP):
        # Determine the x and y of the other point
        xp = otherP.getX()
        yp = otherP.getY()
        
        # Calculate the distance between two points
        distance = ((xp - self.x)**2 + (yp - self.y)**2)**0.5
        
        return distance


# Determine two points and display the distance between them
p1 = Point(3, 3)
p2 = Point(6, 7)
print(format(p2.distanceFromPoint(p1), ',.3f'))
