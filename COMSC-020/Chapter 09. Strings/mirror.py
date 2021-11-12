def get_reverse(string):
    """Take a string and return its reverse."""
    
    reverse = string[::-1]
    
    return reverse


def get_mirror(string):
    """Take a string and return its mirror."""
    
    mirror = string + get_reverse(string)
    
    return mirror


def main():
    """Define main function."""
    
    # Prompt the user for a sentence
    sentence = input('Please enter a sentence: ')
    
    # Determine and display the mirror of the sentence
    mirror_sentence = get_mirror(sentence)
    print(f'Its mirror is "{mirror_sentence}".')

# Call main function
main()
