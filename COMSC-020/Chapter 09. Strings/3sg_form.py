# 
# Problem: https://docs.google.com/document/d/16P8dQrgQlYLcWbDT-CkXmHZ2NSdl44NamDufKDDmK8w/edit?usp=sharing
# 



SPECIAL = 'ochsshxz' # constant

def make_3sg_form(verb):
    ''' Take a verb in infinite form
        Returns its third person singular form. '''
    
    verb = verb.capitalize()
    
    if verb[-1] == 'y':
        verb_3sg = verb[:-1] + 'ies'
    elif verb[-1] in SPECIAL:
        verb_3sg = verb + 'es'
    else:
        verb_3sg = verb + 's'
    
    return verb_3sg


def main():
    ''' define main function. '''
    
    # prompt the user for a verb
    verb = input('Enter a verb in infinitive form: ')
    
    # determine and display the third person singular form of the verb
    verb_3sg = make_3sg_form(verb)
    print(f'Its third person singular form: {verb_3sg}')
    
# call main function    
main()
