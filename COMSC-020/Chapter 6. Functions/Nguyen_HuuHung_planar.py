# Huu Hung Nguyen
# 09/19/2021
# Nguyen_HuuHung_star.py
# Draw a star.


# Define distance function
def distance(x1, y1, x2, y2):
    
    # Calculate distance
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**(1 / 2)
    
    return distance

# Define block distance function
def block_distance(x1, y1, x2, y2):
    
    # Calculate block distance
    block_distance = abs(x1 - x2) + abs(y1 - y2)
    
    return block_distance

# Define main function
def main():
    
    # Prompt user for x and y coordinates of two points
    x1 = float(input('Enter the x coordinate of the point number 1: '))
    y1 = float(input('Enter the y coordinate of the point number 1: '))
    x2 = float(input('Enter the x coordinate of the point number 2: '))
    y2 = float(input('Enter the y coordinate of the point number 2: '))
    
    # Get pythagorean and city block distance
    pythagorean = distance(x1, y1, x2, y2)
    city_block = block_distance(x1, y1, x2, y2)
    
    # Display results
    print(f'''Pythagorean distance = {pythagorean:,.2f}
City block distance = {city_block:,.2f}''')
    
# Call main function
main()