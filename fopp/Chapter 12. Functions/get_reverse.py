# Take string, reverse its string argument, and print result
def get_reverse(string):
    
    # reverse string argument
    for n in range(len(string) - 1, -1, -1):
        print(string[n], end = '')
    
    
# Define main function
def main():
    
    # Prompt user for a string
    string = input('Enter a string: ')
    
    # Obtain reverse string
    result = get_reverse(string)
    
# Call main function
main()
