# Check number and return result
def num_test(num):
    
    # Check number
    if num > 10:
        return 'Greater than 10.'
    elif num < 10:
        return 'Less than 10.'
    else:
        return 'Equal to 10.'


# Define main function
def main():
    
    # Prompt user for a number
    number = float(input('Enter a number: '))
    
    # Check number
    check_number = num_test(number)
    
    # Display result
    print(check_number)
    
# Call main function
main()
