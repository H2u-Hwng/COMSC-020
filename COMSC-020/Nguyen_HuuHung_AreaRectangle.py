# Huu Hung Nguyen
# 09/21/2021
# Nguyen_HuuHung_AreaRectangle.py
# The program prompts the user for the width and height.
# It then calculates the the area of the rectangle and prints the result.


# Prompt user for width and height
width = float(input('Enter the width of the rectangle: '))
height = float(input('Enter the height of the rectangle: '))

# Calculate area of rectangle
area_rectangle = width * height

# Print result
print('The are of the rectangle is {:.3f}.'. format(area_rectangle))