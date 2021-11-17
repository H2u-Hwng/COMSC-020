def is_rightangled(x, y, z):
    '''Take three sides of a triangle
       Return True if the triangle is right-angled and False otherwise.'''

    if abs(z**2 - (x**2 + y**2)) < 0.001:
        rightangled = True
    else:
        rightangled = False
        
    return rightangled
    

def main():
    '''Define main function.'''
    
    # Prompt the user for three sides of the triangle
    side1 = float(input('Please enter the first side of the triangle: '))
    side2 = float(input('Please enter the second side of the triangle: '))
    side3 = float(input('Please enter the longest side of the triangle: '))
    
    # Determine whether the triangle is right-angled
    print(is_rightangled(side1, side2, side3))
    
# Call main function  
main()
