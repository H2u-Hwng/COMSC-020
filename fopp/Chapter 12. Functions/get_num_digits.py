# Take number, and convert integer to string
# Calculate and return number of digits
def get_num_digits(num):
    
    # Convert int to str
    num_str = str(num)
    
    # Calculate number of digits
    digits = len(num_str)
    
    return digits


# Define main function
def main():
    
    # Prompt user for an integer
    number = int(input('Enter an integer: '))
    
    # Obtain number of digits
    num_digits = get_num_digits(number)
    
    # Display result
    print(f'The number of digits in number {number} is {num_digits}.')
    
# Call main function
main()
