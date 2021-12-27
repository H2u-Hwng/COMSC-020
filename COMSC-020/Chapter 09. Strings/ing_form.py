#
# Problem: https://docs.google.com/document/d/1Z6paCNgqkuuCcK9E97pHdmT9uJ-f_OQxwP5_WwApv8g/edit?usp=sharing
#



VOWELS = 'aeiouyw' # constant

def make_ing_form(verb):
    ''' take a verb in infinitive form
        return its present participle form. '''

    verb = verb.capitalize()
    
    if verb[-1] == 'e':
        if verb[-2:] == 'ee' or verb == 'Be':
            verb_ing = verb + 'ing'
        elif verb[-2:] == 'ie':
            verb_ing = verb[:-2] + 'ying'
        else:
            verb_ing = verb[:-1] + 'ing'
    elif verb[-2] in VOWELS:
        verb_ing = verb + verb[-1] + 'ing'
    else:
        verb_ing = verb + 'ing'
    
    return verb_ing
    
     
def main():
    ''' define main function. '''
    
    # prompt the user for a verb in infinitive form
    verb = input('Enter a verb in infinitive form: ')
     
    # determine and display the verb in present participle form
    verb_ing = make_ing_form(verb)
    print(f'Its present participle form: {verb_ing}')
    
# call main function
main()
