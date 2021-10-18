# Library
import random

# Take numbers list, count and return odd numbers
def count_odd(num_list):
    
    # Count odd numbers in numbers list
    count = 0
    for n in num_list:
        if n % 2 != 0:
            count += 1 
    
    return count


# Take numbers list, calculate and return sum of all even numbers
def sum_even(num_list):
    
    # Sum up all even numbers in numbers list
    total_even = sum([n for n in num_list if n % 2 == 0])
    
    return total_even


# Take numbers list, calculate and return sum of all negative numbers
def sum_negative(num_list):
    
    # Sum up all negative numbers in numbers list
    total_negative = sum([n for n in num_list if n < 0])
    
    return total_negative


# Define main function
def main():
    
    # Prompt user for quantity and value of numbers list
    quantity = int(input('What is the quantity of the numbers list? '))
    numbers_list = [random.randint(-1000, 1000) for _ in range(quantity)]
    
    # Obtain the number of odd numbers
    count_odd_numbers = count_odd(numbers_list)
    
    # Obtain the sum of all even numbers
    sum_even_numbers = sum_even(numbers_list)
    
    # Obtain the sum of all negative numbers
    sum_negative_numbers = sum_negative(numbers_list)
    
    # Display results
    print(f'''The numbers list is {numbers_list}.
There are {count_odd_numbers} odd numbers in the numbers list.
The sum of all the even numbers in the numbers list is {sum_even_numbers}.
The sum of all the negative numbers in the numbers list is \
{sum_negative_numbers}.''')
    
# Call main function
main()
