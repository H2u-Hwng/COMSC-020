# Library
import random

# Define main function
def main():
    
    # Prompt users for quantity of numbers
    quantity = int(input("How many numbers will be on the list? "))
    
    # Initialize odd count, lists of odd, even, and negative numbers
    odd_count = 0
    odd_numbers_list = []
    even_numbers_list = []
    neg_numbers_list = []
    
    for n in range(quantity):
        
        # Determine number in range -1000 to 1000
        number = random.randint(-1000, 1000)
        
        # Check if number is odd 
        if number % 2 != 0:
            odd_count += 1
            odd_numbers_list.append(number)
            
        # Check if number is even
        if number % 2 == 0:
            even_numbers_list.append(number)
            
        # Check if number is negative
        if number < 0:
            neg_numbers_list.append(number)
    
    # Calculate sum total even numbers and sum total negative numbers
    sum_even = sum(even_numbers_list)
    sum_negative = sum(neg_numbers_list)
    
    # Display results
    print(f"There are {odd_count} odd numbers in {odd_numbers_list}.")
    print(f"Sum total even numbers in {even_numbers_list} is {sum_even}.")
    print(f"Sum total negative numbers in {neg_numbers_list} is {sum_negative}.")

# Call main function
main()
