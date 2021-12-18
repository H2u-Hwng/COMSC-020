def get_initial(string):
    ''' Take a string and return its upper initial. '''
    
    return string[0].upper()


def main():
    ''' Define main function. '''
    
    # Prompt the user for the full name
    full_name = input("Enter a person's first, middle, and last names: ")

    # Initialize the initials
    initials = ''

    # Create a list of words having in the full name
    words_list = full_name.strip().split()

    # Check each word in the words list
    for word in words_list:
        initials += get_initial(word)

    # Display the initials
    print(initials)

# Call main function
main()
