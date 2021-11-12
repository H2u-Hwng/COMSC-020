def get_reverse(string):
    """Take a string and return its reverse."""
    
    reverse = string[::-1]
    
    return reverse


def main():
    """Define main function."""
    
    # Prompt the user for a sentence
    sentence = input('Please enter a sentence: ')
    
    # Determine and display the reverse of the sentence
    reverse_sentence = get_reverse(sentence)
    print(f'Its reverse is {reverse_sentence}.')

# Call main function
main()
