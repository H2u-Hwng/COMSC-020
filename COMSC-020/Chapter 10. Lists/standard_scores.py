# Huu Hung Nguyen
# 12/06/2021
# Nguyen_HuuHung_scores.py
# The program takes a numbers list and returns a new list of standard scores.
# It then display the the list of standard scores.

# Library
import math

def get_sum(data_list, exponent):
    ''' Take a data lsit and an exponent
        Return the sum of data list with the exponent of each data. '''
    
    # Inititalize a sum
    sum = 0
    
    for data in data_list:
        # Add the exponent of each data to the sum
        sum += data**exponent

    return sum


def stdev(data_list):
    ''' Take a data list and return its standard deviation. '''
    
    # Determine the number having in the data list
    n = len(data_list)
    
    # Check whether the data list is empty
    if n == 0 or n == 1:
        deviation = 0
    else:
        # Determine 2 sum having in the standard deviation formula
        sum1 = get_sum(data_list, 2)
        sum2 = get_sum(data_list, 1)
        
        # Determine the standard deviation
        deviation = math.sqrt((n * sum1 - sum2**2) / (n * (n - 1)))

    return deviation


def mean(data_list):
    ''' Take a data list and return its average. '''
    
    # Determine the number having in the data list
    n = len(data_list)
    
    # Check whether the data list is empty
    if n == 0:
        average = 0
    else:
        # Determine the average of the data list
        average = sum(data_list) / n
    
    return average


def standardize(data_list):
    ''' Take a data list and return its standard scores. '''
    
    # Determine the average of the data list
    average = mean(data_list)
    
    # Determine the deviation of the data list
    deviation = stdev(data_list)
    
    # Initialize a list of the standard scores
    standard_scores = []
    
    # Check whether the deviation is 0
    if deviation == 0:
        standard_scores = data
    else:
        for data in data_list:
            # Determine the standard score of each data
            standard_score = (data - average) / deviation
            
            # Add the score to the end of the standard scores list 
            standard_scores.append(format(standard_score, '.3f'))

    return standard_scores


def main():
    ''' Define main function. '''
    
    # Prompt the user for a list of numbers separated by a comma
    input_prompt = 'Enter numbers separated by a comma: '
    alist = [float(number) for number in input(input_prompt).split(',')]
    
    # alist = [47.0, 11.0, 10.0, 66.0, 8.5]
    
    # Determine the standard scores
    standard_scores = standardize(alist)
    
    # Display the standard scores
    print(alist)
    print('-----Generate to standard scores-----')
    print('[{}]'. format(', '. join(standard_scores)))
    
# Call main function
main()
