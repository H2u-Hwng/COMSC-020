def remove_letter(letter, string):
    """Removes all occurrences of a given letter from a string."""
    
    string_without_letter = string.replace(letter, '')
    
    return string_without_letter


def main():
    """Define main function."""
    
    # Prompt the user for a word
    word = input('Please enter a word: ')
    
    # Prompt the user for a letter
    letter = input('Please enter a letter you want to remove from the word: ')
    
    # Determine and display the word without the letter
    word_without_letter = remove_letter(letter, word)
    print('The word "{}" without the letter "{}" will become "{}".'.
          format(word, letter, word_without_letter))

# Call main function
main()
