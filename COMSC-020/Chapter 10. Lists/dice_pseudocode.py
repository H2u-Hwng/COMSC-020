# Ask the user how many times they wish to toss a pair of dice, from 1-999.
# 
# Simulate randomly tossing a pair of dice as many times as the user requested,
# creating a 6 x 6 list showing how often each combination of dice was rolln.
# 
# Then calculate the frequencies for each total of dice.


def get_n_rolls():
    result = 0
    valid = False
    while not valid:
        prompt and read # of rolls
        if not valid input:
            print appropriate error message
    return result

def roll_dice(n_rolls):
    """
    1) Create a 6 by 6 two-dimensional list (call it rolls)
       filled with all zeros.
    2) Use a loop that iterates n_rolls times:
        2a) Generate two random numbers in the range 0-5
        2b) Use those numbers as indices to the rolls[][] list
            and add one to the corresponding list entry
    """
    return rolls
    
def print_rolls(rolls):
    """Use a nested loop to print the given 2-d list of dice rolls"""
    
def calc_frequencies(rolls):
    """
       1) Create a list of length 11 named totals with all zeros in it
       2) Go through the rolls[][] list with a nested loop;
          add the number in rolls[row][col] to the appropriate entry in the
          totals list.
     """   
    return totals
    
def main():
    """
    1) Get the number of dice rolls (call it n_rolls)
    2) Call roll_dice with n_rolls as a parameter; the result
        goes into a two-dimensional list (call it rolls)
    3) Send that list to print_rolls() to print the number
        of rolls for each combination of the two dice
    4) Send the list from step 2 to calc_frequencies() and store
        the result in an list (call it totals)
    5) Print the result of step 4.
    """
    
main()

