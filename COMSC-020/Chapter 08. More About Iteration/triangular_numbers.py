def print_triangular_numbers(number):
    '''Take a number and print its triangular numbers.'''
    
    for n in range(1, number + 1):
        print(f'{n}       {n * (n + 1) / 2:.0f}')
        
    
def main():
    '''Define main function.'''
    
    # Prompt user for a number
    number = int(input('Please enter a number: '))
    
    # Display its triangular numbers
    print_triangular_numbers(number)
    
main()
