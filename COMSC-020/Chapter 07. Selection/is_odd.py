def is_odd(n):
    '''Return True if the number is odd and False otherwise.'''
    
    if n % 2 != 0:
        odd = True
    else:
        odd = False
        
    return odd


def main():
    '''Define main function.'''
    
    # Prompt the user for a number
    number = float(input('Please enter a number: '))
    
    # Determine whether the number is even
    print(is_odd(number))
    
# Call main function
main()
