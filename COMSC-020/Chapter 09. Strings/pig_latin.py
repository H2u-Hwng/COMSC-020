# Huu Hung Nguyen
# 11/10/2021
# Nguyen_HuuHung_pig_latin.py
# Program prompts user for a sentence.
# Program contains function converting sentence to pig latin.
# It then displays result.

# Constants for vowels
VOWELS = "aeiouyAEIOUY"

# Convert word to pig latin and return new word
def to_pig_latin(word):
    
    # Initialize position
    position = 0
    
    # Check if the first letter of word is in vowels
    if word[0] in VOWELS:
        # Check if first letter of word is Y or y
        if word[0] in "yY":
            position += 1
            
            # Add 1 to position until finding position of vowel in word
            while word[position] not in VOWELS and position < len(word):
                position += 1
            new_word = word[position:] + word[:position] + 'ay'
        else:
            new_word = word + "way" 
    else:
        # Check if first 2 letters of word is qu or Qu
        if word[:2] in "quQu":
            position += 2
            
        # Add 1 to position until finding position of vowel in word
        while word[position] not in VOWELS and position < len(word):
            position += 1
        new_word = word[position:] + word[:position] + 'ay'
    
    # Check if the first letter of word is uppercase
    if word[0].isupper():
        new_word = new_word.capitalize()
    
    return new_word
      
      
# Define main function
def main():
    again = True
    
    # Convert sentence to pig latin until users enter a new line
    while again:
        
        # Get a sentence from the user
        sentence = input('Please enter a sentence: ')
        
        # Split the sentence into a list of words
        words_list = sentence.split()
        
        # Create result
        pig_sentence = ''
        
        # Check if users enter a new line
        if sentence == '':
            again = False
        else:
            for word in words_list:
                # Convert word to pig latin
                pig_word = to_pig_latin(word)
                # Obtain result
                pig_sentence += pig_word + ' '
            
            # Display result
            print(pig_sentence)
        
# Call main function
main()
