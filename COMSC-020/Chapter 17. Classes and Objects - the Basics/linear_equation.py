class Point:
    ''' Point class for representing and manipulating x, y coordinates. '''
    
    def __init__(self, initX, initY):
        ''' Create a new point at the given coordinates. '''
        
        self.x = initX
        self.y = initY
        
    def getX(self):
        ''' Return x. '''
        
        return self.x
    
    def getY(self):
        ''' Return y. '''
        
        return self.y
    
    def get_line_to(self, otherP):
        ''' Return the slope and constant of the linear equation. '''
        
        # Determine the numerator and denominator of the slope
        numerator = otherP.y - self.y
        denominator = otherP.x - self.x
        
        # Check whether the denominator is 0
        if denominator == 0:
            result = 'The linear equation is undefined.'
        else:
            # Determine the slope and constant
            slope = numerator / denominator
            constant = self.y - self.x * slope
            
            # Determine the result
            result = slope, constant
            
        return result
    
    
# Determine 3 points and display their slopes and constants
print(Point(4, 11).get_line_to(Point(6, 15)))
print(Point(4, 11).get_line_to(Point(4, 15)))
print(Point(4, 11).get_line_to(Point(6, 11)))
