# Take string, mirrors its string argument, and print result
def get_mirror(string):
    
    # mirrors string argument
    result = string + string[::-1]
    
    return result


# Define main function
def main():
    
    # Prompt user for a string
    astring = input('Enter a string: ')
    
    # Obtain mirror string
    mirror = get_mirror(astring)
    
    # Display mirror
    print(mirror)
    
# Call main function
main()
