# Problem: https://docs.google.com/document/d/1NSl2yiTzoQ8d0y_D2BlQUB4Q7uPqxVE1p-bQyQDXmZk/edit?usp=sharing

import random # library

def roll_dice():
    ''' Return result of randomly rolling two dice. '''
    
    randoms_list = [random.randint(1,6) for _ in range(2)]
    
    return randoms_list


def get_n():
    ''' Use while loop to repeatedly ask for number of
    times to roll dice (between 1 and 100 inclusive).
    Return the number. '''
    
    valid = False
    while not valid:
        n = int(input('Enter a number of times to roll dice (1-100): '))
        if n in range(1, 101):
            valid = True
        else:
            print('Please enter a valid number! \n')
    
    return n


def main():
    ''' define main function. '''
    
    frequency = [0 for _ in range(13)] # make variable frequency a list of 13 zeros
    
    n_tosses = get_n() # ask for number of times to roll dice
    
    for toss in range(n_tosses):
        roll = roll_dice()
       
        # add 1 to the number at that place in the frequency list
        frequency[sum(roll)] += 1
        
    # display the bar chart
    for index in range(2, 13):
        print(f'{index:2d}', end = ' ')
        
        for _ in range(frequency[index]):
            print('@', end = '')
            
        print() # for readability
         
# call main function
main()
