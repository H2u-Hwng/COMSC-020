# Huu Hung Nguyen
# 10/06/2021
# area_circle_def.py
# The program prompt the user for the radius.
# It then computes the area of a circle and prints the result.

# Library
import math

# Define get area function
def get_area(radius):
    
    # Calculate area of circle
    area = math.pi * radius**2
    
    return area
    
# Define main function
def main():
    
    # Prompt user for radius
    radius = float(input('Enter the radius: '))
    
    # Call get area function
    area = get_area(radius)
    
    # Display msg with area
    print(f'The area of the circle having radius {radius} is {area:,.3f}.')
    
# Call main function
main()