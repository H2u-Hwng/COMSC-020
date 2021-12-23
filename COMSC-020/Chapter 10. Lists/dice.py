# Huu Hung Nguyen
# 12/07/2021
# Nguyen_HuuHung_dice.py
# Ask the user how many times they wish to toss a pair of dice, from 1-999.
# 
# Simulate randomly tossing a pair of dice as many times as the user requested,
# creating a 6 x 6 list showing how often each combination of dice was rolln.
# 
# Then calculate the frequencies for each total of dice.

# Library
import random

def get_n_rolls():
    ''' Return the number rolls. '''
    
    valid = False
    
    # Keeping asking until the number rolls is valid
    while not valid:
        # Prompt the user for the times rolling
        input_prompt = 'How many times do you want to roll the dice (1-999)? '
        n_rolls = int(input(input_prompt))
        
        # Check whether the user inputs valid numbers
        if n_rolls not in range(1, 1000):
            print('ERROR! Please enter the number is in range. \n')
        else:
            valid = True
            
    return n_rolls


def roll_dice(n_rolls):
    """
    1) Create a 6 by 6 two-dimensional list (call it rolls)
       filled with all zeros.
    2) Use a loop that iterates n_rolls times:
        2a) Generate two random numbers in the range 0-5
        2b) Use those numbers as indices to the rolls[][] list
            and add one to the corresponding list entry
    """

    # Initialize a 6 by 6 two-dimensional list
    rolls = [[0 for column in range(6)] for row in range(6)]
    
    #
    for n in range(n_rolls):
        rand1 = random.randint(0,5)
        rand2 = random.randint(0,5)
        
        # Add 1 to the corresponding list entry of 2 random numbers
        rolls[rand1][rand2] += 1
        
    return rolls
    
    
def print_rolls(rolls):
    """Use a nested loop to print the given 2-d list of dice rolls"""
    
    print('Frequencies for individual dice')
    print('      1   2   3   4   5   6')
    print('    ------------------------')
    
    #
    for i in range(6):
        print(f'{i + 1}|', end = '   ')
        
        #
        for roll in rolls[i]:
            print(f'{roll:2d}', end = '  ')
            
        print()
    
    
def calc_frequencies(rolls):
    """
       1) Create a list of length 11 named totals with all zeros in it
       2) Go through the rolls[][] list with a nested loop;
          add the number in rolls[row][col] to the appropriate entry in the
          totals list.
     """
    
    # Initialize a list of length 11 named totals
    totals = [0 for _ in range(11)]
    
    # Add the number in rolls[row][col] to the corresponding number 
    for row in range(6):
        for col in range(6):
            totals[row + col] += rolls[row][col]
    
    return totals
    
    
def main():
    """
    1) Get the number of dice rolls (call it n_rolls)
    2) Call roll_dice with n_rolls as a parameter; the result
        goes into a two-dimensional list (call it rolls)
    3) Send that list to prin_rolls() to print the number
        of rolls for each combination of the two dice
    4) Send the list from step 2 to calc_frequencies() and store
        the result in an list (call it totals)
    5) Print the result of step 4.
    """
    
    # Get the number of dice rolls
    n_rolls = get_n_rolls()
    
    # Determine and display the two-dimensional list
    rolls = roll_dice(n_rolls)
    
    print_rolls(rolls)
    
    print()
    
    # Determine and display the frequencies of totals
    totals = calc_frequencies(rolls)
    
    print('Frequencies of totals')
    
    #
    for i in range(11):
        print(f'{i + 2:2d}:  {totals[i]:3d}')

# Call main function
main()
