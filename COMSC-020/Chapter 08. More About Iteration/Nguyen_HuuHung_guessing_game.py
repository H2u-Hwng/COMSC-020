# Huu Hung Nguyen
# 10/26/2021
# Nguyen_HuuHung_guessing_game.py
# Constants for first and last numbers.
# Program generates a random number in the range of first and last numbers.
# Program contains function that repeatedly asks users to guess a number
# from 1-100, or enter 0 to finish.
# It then asks the player if they want to play again.

# Library
import random

# Constants for first and last numbers
FIRST_NUM = 1
LAST_NUM = 100

# Repeatedly ask users to guess a number from 1-100, or enter 0 to finish
def play_guessing_game(number):
    finish = False
    
    # Initialize counting of the number of guesses that the user makes
    counting = 0
    
    print('Guess my number!')
    
    input_prompt = 'Guess a number from ' + str(FIRST_NUM) + ' to ' + \
                   str(LAST_NUM) + ', or enter 0 to quit guessing: '
    
    # Enter guessing number until users guess correct or enter 0
    while not finish:
        guessing = int(input(input_prompt))
        
        # Check for guessing number
        if guessing == number:
            print('Congratulations!', end = ' ')
            print(f'You guessed the right number in {counting} guesses! \n')
            finish = True
        elif guessing == 0:
            print(f"You didn't guess my number (it was {number}). \n")
            finish = True
        else:
            if guessing < number:
                print('Too low, try again.')
            else:
                print('Too high, try again.')
            counting += 1
            
            
# Define main function
def main():
    again = 'Y'
    
    # Enter number until users enter N)o
    while again == 'Y':
        
        # Generate a random number in the range of 1 through 100
        number = random.randint(FIRST_NUM, LAST_NUM)
        
        # Obtain play guessing game
        play_guessing_game(number)
        
        again = input('Do you want to play again (y/n)? ')
        again = again.upper()
        
        # Check if users enter N)o
        if again == 'N':
            print('Goodbye. Thanks for playing.')
            
# Call main function      
main()