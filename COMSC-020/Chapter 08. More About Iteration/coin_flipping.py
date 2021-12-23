# coin_flip.py

# This program repeatedly "flips a coin" by generating a random
# integer 0 (heads) or 1 (tails). The user then gets to guess
# the flip by entering H or T, or quit by entering Q.

# After each flip, the program tells the player what the flip was
# and whether they guessed right or wrong.

# When the player quits, the program tells the player how many
# flips they guessed right and how many wrong.

# Library
import random

# Prompt user for 'H', 'T', or 'Q'. Validate user input. Return input
def get_response():
    valid = False
    print("I flipped a coin. ")
    
    # Enter response until users enter a valid input ('H', 'T', or 'Q')
    while not valid:
        response = input("Guess H)eads, T)ails, or Q)uit: ")
        response = response.upper()
        
        # Check for valid input ('H', 'T', or 'Q')
        if response in ['H', 'T', 'Q']:
            valid = True
        else:
            print(f"I don't understand '{response}'.")
    
    return response


# Define main function
def main():
    
    # Initialize variables for the number of correct and incorrect guesses
    num_correct = 0
    num_incorrect = 0
    
    guess = "" 
    
    # Keep flipping the coin and having the user guess until the user enter Q
    while guess != "Q":
        
        # Generate a random number 0 (heads) or 1 (tails)
        flip = random.randint(0, 1)
         
        # Determine what the coin flip was
        if flip == 0:
            correct_answer = 'H'
            coin_word = "heads"
        else:
            correct_answer = 'T'
            coin_word = "tails"
        
        # Obtain the user's guess or Q for quit
        guess = get_response()
        
        # If not quitting, determine rather guessed correctly
        if guess != 'Q':
            print(f"The coin came up {coin_word}.")
            
            # Determine rather guess is correct or incorrect
            if guess == correct_answer:
                print("You guessed right! \n")
                num_correct += 1
            else:
                print("Sorry, you guessed wrong. \n")
                num_incorrect += 1
            
    # Display number of correct and incorrect guesses    
    print('Number of correct guesses:', num_correct)
    print('Number of incorrect guesses:', num_incorrect)
    
# Call main function
main()
