# Sum all the elements in a list up to;
# but not including the first even number.

# Library
import random

# Calculate sum total of numbers list without the first even number
def get_sum_total(quantity):
    
    # Initialize numbers list
    numbers_list = []

    # Append numbers to list
    for _ in range(quantity):
        numbers_list.append(random.randint(0, 1000))
           
    # Remove first even number
    for n in numbers_list:
        if n % 2 == 0:
            numbers_list.remove(n)
            break
        
    # Calculate sum total 
    sum_total = sum(numbers_list)
    
    return numbers_list, sum_total


# Define main function
def main():
    
    # Prompt user for quantity of numbers in list
    quantity = int(input("how many numbers will be on the list? "))
    
    # Obtain numbers_list and sum total
    numbers_list, sum_total = get_sum_total(quantity)

    result_prompt = "Sum all the elements in " + str(numbers_list) + \
                    " is " + str(sum_total) + "."
    
    # Display sum numbers in list
    print(result_prompt)

# Call main function
main()
