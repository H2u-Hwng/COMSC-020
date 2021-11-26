# Constant for a pirate traslations dictionary
PIRATE_TRANSLATIONS = {'sir' : 'matey',
                       'hotel' : 'fleabag inn',
                       'student' : 'swabbie',
                       'boy' : 'matey',
                       'madam' : 'proud beauty',
                       'professor' : 'foul blaggart',
                       'restaurant' :'galley',
                       'your' : 'yer',
                       'excuse' : 'arr',
                       'students' : 'swabbies',
                       'are' : 'be',
                       'lawyer' : 'foul blaggart',
                       'the' : 'th’',
                       'restroom' : 'head',
                       'my' : 'me',
                       'hello' : 'avast',
                       'is' : 'be',
                       'man' : 'matey'}

def translator(english):
    ''' Take a sentence in English and convert it to in Pirate
        Return the sentence in Pirate. '''
    
    # Initialize a sentence in Pirate
    pirate = ''
    
    # Determine the clean sentence in English
    clean_english = clean_sequence(english)
    
    for word in clean_english.split():
        # Add English's corresponding Pirate to the end
        pirate += PIRATE_TRANSLATIONS.get(word, word) + ' '
        
    # Strip whitespace off the end
    pirate = pirate.strip()
    
    return pirate


def clean_sequence(string):
    ''' Take a string
        Return the string no punctuation and all words in lowercase. '''
    
    clean_string = string.strip('.').lower()
    
    return clean_string


def main():
    ''' Define main function. '''
    
    # Prompt user for a sentence in English
    english = input('Please enter a sentence in English: ')
    
    # Determine and display the sentence in Pirate
    pirate = translator(english)
    print(pirate)

# Call main function
main()
