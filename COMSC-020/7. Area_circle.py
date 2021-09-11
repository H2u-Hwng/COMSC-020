# Huu Hung Nguyen
# 09/10/2021
# Area_circle.py
# The program prompt the user for the radius.
# It then computes the area of a circle and prints the result.


# Library
import math

# Prompt user for radius
radius = float(input('Enter the radius: '))

# Compute area
area = math.pi * radius**2

# Print the result
print('The area of the circle having radius {:,.3f} is {:,.3f}.'
      .format(radius, area))
