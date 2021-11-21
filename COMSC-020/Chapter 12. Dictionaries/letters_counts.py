# Constant for the alphabet
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def counting_letters(string):
    '''Take a string and count the alphabet in the string
       Return the dictionary of letters and counts.'''
    
    # Convert the string to all lowercase
    string = string.lower()
    
    # Initialize the empty dictionary of letters and counts
    letters_counts = {}
    
    for char in string:
        # Check whether the character is in the alphabet
        if char in ALPHABET:
            # Check whether the character is in the dictionary
            if char in letters_counts:
                letters_counts[char] += 1
            else:
                letters_counts[char] = 1
    
    return letters_counts


def main():
    '''Define main function.'''
    
    # Prompt the user for a sentence
    sentence = input('Please enter a sentence: ')
    
    # Determine the dictinary of letters and counts
    letters_counts = counting_letters(sentence)
    
    # Display letters and counts in the sorted dictionary
    for letter, count in sorted(letters_counts.items()):
        print(letter, count)

# Call main function
main()
