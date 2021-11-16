def get_reverse(string):
    '''Take a string and return its reverse.'''
    
    reverse_string = string[::-1]
    
    return reverse_string


def is_palindrome(string):
    '''Return True if string is palindrome and False otherwise.'''
    
    if string == get_reverse(string):
        palindrome = True
    else:
        palindrome = False
    
    return palindrome


def clean_sequence(string):
    '''Take a string and clean sequence of the string
       Return the new string.'''
    
    new_string = string.replace(' ', '').lower()
    
    return new_string
            
            
def main():
    '''Define main function.'''
    
    # Prompt user for a sentence
    sentence = input('Please enter a sentence: ')
    
    # Determine new sentence
    new_sentence = clean_sequence(sentence)
    
    # Display result 
    print(is_palindrome(new_sentence))

# Call main function
main()
