# Huu Hung Nguyen
# 10/12/2021
# Nguyen_HuuHung_planar.py
# The program contains 2 functions calculating distance and block distance.
# It prompts user for the x and y coordinates of two points.
# It then displays distance and block distance.

# Calculate and return distance
def distance(x1, y1, x2, y2):
    
    # Calculate distance
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    
    return distance


# Calculate and return block distance
def block_distance(x1, y1, x2, y2):
    
    # Calculate block distance
    block_distance = abs(x1 - x2) + abs(y1 - y2)
    
    return block_distance
    
    
# Define main function
def main():
    
    # Prompt user for the x and y coordinates of two points
    x1_coord = float(input('Enter the x coordinate of point 1: '))
    y1_coord = float(input('Enter the y coordinate of point 1: '))
    
    x2_coord = float(input('Enter the x coordinate of point 2: '))
    y2_coord = float(input('Enter the y coordinate of point 2: '))
    
    # Obtain pythagorean distance and city block distance
    pythagorean_distance = distance(x1_coord, y1_coord, x2_coord, y2_coord)
    city_block_distance = \
                    block_distance(x1_coord, y1_coord, x2_coord, y2_coord)
    
    # Display pythagorean distance and city block distance
    print(f'The Pythagorean distance is {pythagorean_distance:,.2f}')
    print(f'The "city block" distance is {city_block_distance:,.2f}')
    
# Call main function
main()