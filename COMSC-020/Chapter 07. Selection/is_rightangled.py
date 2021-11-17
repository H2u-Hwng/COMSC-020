def sum_squared_sides(x, y):
    '''Take two sides of a triangle and calculate the sum squared sides
       Return sum squared sides.'''
    
    sum_squared = x**2 + y**2
    
    return sum_squared
    
    
def is_rightangled(x, y, z):
    '''Take three sides of a triangle
       Return True if the triangle is right-angled and False otherwise.'''
    
    # Determine min side, side, and max side of the triangle
    min_side, side, max_side = sorted([x, y, z])
    
    if abs(max_side**2 - sum_squared_sides(min_side, side)) < 0.001:
        rightangled = True
    else:
        rightangled = False
        
    return rightangled
    

def main():
    '''Define main function.'''
    
    # Prompt the user for three sides of the triangle
    side1 = float(input('Please enter the first side of the triangle: '))
    side2 = float(input('Please enter the second side of the triangle: '))
    side3 = float(input('Please enter the third side of the triangle: '))
    
    # Determine whether the triangle is right-angled
    print(is_rightangled(side1, side2, side3))
    
# Call main function  
main()
