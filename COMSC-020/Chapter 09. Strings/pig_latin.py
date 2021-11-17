# Huu Hung Nguyen
# 11/12/2021
# Nguyen_HuuHung_pig_latin.py
# Program prompts user for a sentence.
# Program contains function converting sentence to pig latin.
# It then displays result.

# Constant for vowels
VOWELS = 'aeiouyAEIOUY'

def to_pig_latin(word):
    '''Take a word and covert to its pig latin
       Return pig latin word.'''
    
    # Initialize position
    position = 0
    
    # Check if the first letter of word is in vowels
    if word[0] in VOWELS:
        # Check if the first letter of word is y or Y
        if word[0] in 'yY':
            position += 1
            
            # Add 1 to position until finding position of vowel in word
            while word[position] not in VOWELS and position < len(word):
                position += 1
            
            new_word = word[position:] + word[:position] + 'ay'
        else:
            new_word = word + 'way'
    else:
        # Check if first 2 letters of word is qu or Qu
        if word[:2] in 'quQu':
            position += 2
            
        # Add 1 to position until finding position of vowel in word
        while word[position] not in VOWELS and position < len(word):
            position += 1
            
        new_word = word[position:] + word[:position] + 'ay'
    
    # Check if the first letter of word is uppercase
    if word[0].isupper():
        new_word = new_word.capitalize()
    
    return new_word
      
      
def main():
    '''Define main function.'''
    
    again = True
    
    # Convert sentence to its pig latin until users enter a new line
    while again:
        
        # Prompt the user for a sentence
        sentence = input('Please enter a sentence: ')
        
        # Split words of sentence into the words list
        words_list = sentence.split()
        
        # Initialize pig latin translation
        pig_sentence = ''
        
        # Check if users enter a new line
        if sentence == '':
            again = False
        else:
            for word in words_list:
                # Convert word to pig latin word
                pig_word = to_pig_latin(word)
                
                # Determine pig latin sentence
                pig_sentence += pig_word + ' '
            
            # Display pig latin translation
            print(pig_sentence)
        
# Call main function
main()
