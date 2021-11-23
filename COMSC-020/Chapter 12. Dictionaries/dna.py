# Huu Hung Nguyen
# 11/23/2021
# Nguyen_HuuHung_dna.py
# Constant for the dictionary of nucleotides and aminos.
# The program prompts the user for a string of ACGT triples.
# It then produces a list of the triples and the corresponding amino acids,
# one set per line until the user just presses ENTER.

# Constant for the dictionary of nucleotides and aminos
NUCLEOTIDES_AMINOS = {'TTT':'Phe', 'TCT':'Ser', 'TGT':'Cys', 'TAT':'Tyr',
                      'TTC':'Phe', 'TCC':'Ser', 'TGC':'Cys', 'TAC':'Tyr',
                      'TTG':'Leu', 'TCG':'Ser', 'TGG':'Trp', 'TAG':'***',
                      'TTA':'Leu', 'TCA':'Ser', 'TGA':'***', 'TAA':'***',
                      'CTT':'Leu', 'CCT':'Pro', 'CGT':'Arg', 'CAT':'His',
                      'CTC':'Leu', 'CCC':'Pro', 'CGC':'Arg', 'CAC':'His',
                      'CTG':'Leu', 'CCG':'Pro', 'CGG':'Arg', 'CAG':'Gln',
                      'CTA':'Leu', 'CCA':'Pro', 'CGA':'Arg', 'CAA':'Gln',
                      'GTT':'Val', 'GCT':'Ala', 'GGT':'Gly', 'GAT':'Asp',
                      'GTC':'Val', 'GCC':'Ala', 'GGC':'Gly', 'GAC':'Asp',
                      'GTG':'Val', 'GCG':'Ala', 'GGG':'Gly', 'GAG':'Glu',
                      'GTA':'Val', 'GCA':'Ala', 'GGA':'Gly', 'GAA':'Glu',
                      'ATT':'Ile', 'ACT':'Thr', 'AGT':'Ser', 'AAT':'Asn',
                      'ATC':'Ile', 'ACC':'Thr', 'AGC':'Ser', 'AAC':'Asn',
                      'ATG':'Met', 'ACG':'Thr', 'AGG':'Arg', 'AAG':'Lys',
                      'ATA':'Ile', 'ACA':'Thr', 'AGA':'Arg', 'AAA':'Lys'}

def is_complete_triple(string):
    '''Take a string
       Return True if the string is complete triple and False otherwise.'''
    
    complete_triple = len(string) % 3 == 0
    
    return complete_triple
    
    
def clean_sequence(string):
    '''Take a string and convert alphabetics to uppercase,
       and add them to the end of the alpha string
       Return the alpha string.'''
    
    # Initialize the alpha string
    alpha_string = ''
    
    for char in string:
        # Check whether the character is alpha 
        if char.isalpha():
            # Convert to uppercase and add to the end of the alpha string
            alpha_string += char.upper()
            
    return alpha_string
    

def main():
    '''Define main function.'''
    
    again = True
    
    # Prompt the users until they press ENTER to quit
    while again:
        input_prompt = 'Enter a nucleotide sequence, ' + \
                       'or just press ENTER to quit: '
        # Prompt the user for nucleotides
        nucleotides = input(input_prompt)
        
        # Check if the user presses ENTER to quit
        if nucleotides == '':
            again = False
        else:
            # Determine nucleotides without non-letters and lowercase
            clean_nucleotides = clean_sequence(nucleotides)
            
            # Check whether the user inputs the complete triples
            if is_complete_triple(clean_nucleotides):
                # Initialize position
                position = 0
                
                for num in range(0, len(clean_nucleotides), 3):
                    # Determine the triple in the clean nucleotides
                    triple = clean_nucleotides[num : num + 3]
                    
                    # Determine the amino acid in the dictionary
                    amino_acid = \
                            NUCLEOTIDES_AMINOS.get(triple, 'invalid sequence')
                    
                    # Display the triple and corresponding amino acid
                    print(triple, amino_acid)
                
                print()
            else:
                print('Error: You must give complete triples. \n')
                
# Call main function
main()
