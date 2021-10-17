# Take numbers list, calculate and return sum of squares of numbers list
def sum_of_squares(num_list):
    
    # Calculate sum of squares of numbers list
    total = sum([n**2 for n in num_list])
    
    return total


# Define main function
def main():
    
    # Prompt user for numbers list
    numbers_list = [float(n) for n in input
                ('Enter numbers list (split by ","): ').split(',')]
    
    # Obtain sum of squares of numbers list
    total_value = sum_of_squares(numbers_list)
    
    # Display sum of squares of numbers list
    print(f'The sum of squares of the numbers in the list {numbers_list} \
is {total_value :,.0f}.')
    
# Call main function
main()
