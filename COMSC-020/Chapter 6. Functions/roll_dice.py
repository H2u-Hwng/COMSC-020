# Library
import random

# Constants for the minimum and maximum random numbers
MIN = 1
MAX = 6

# Define roll dice function
def roll_dice():
    
    # Create a variable to control the loop
    again = 'y'
    
    # Roll dice
    while again == 'y' or again == 'Y':
        print('Rolling the dice ...')
        dice1 = random.randint(MIN, MAX)
        dice2 = random.randint(MIN, MAX)
        
        print('Their values are:')
        print(dice1)
        print(dice2)
        
        print('The sum of the dice: ', dice1 + dice2)
        print('')
        
        # Do another roll of the dice
        again = input('Roll the again? (y = yes): ')

# Call roll dice function       
roll_dice()