def is_prime(n):
    '''Take a number
       Return True if it is a prime number and False otherwise.'''
    
    prime = True
    
    for i in range(2, n):
        if n % i == 0:
            prime = False
    
    return prime
    

def main():
    '''Define main function.'''
    
    # Prompt user for a number
    number = int(input('Please enter an integer number: '))
    
    # Determine and display the prime number
    prime_number = is_prime(number)
    print(prime_number)

# Call main function
main()
