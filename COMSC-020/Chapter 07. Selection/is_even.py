def is_even(n):
    '''Return True if the number is even and False otherwise.'''
    
    if n % 2 == 0:
        even = True
    else:
        even = False
        
    return even


def main():
    '''Define main function.'''
    
    # Prompt the user for a number
    number = float(input('Please enter a number: '))
    
    # Determine whether the number is even
    print(is_even(number))
    
# Call main function
main()
