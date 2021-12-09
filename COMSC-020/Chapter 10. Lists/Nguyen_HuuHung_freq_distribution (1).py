# Huu Hung Nguyen
# 12/07/2021
# Nguyen_HuuHung_freq_distribution.py
# The program takes a numbers list and creates a frequency distribution table.
# It then display the frequency distribution table.

def get_max(data_list):
    ''' Take a data list and return its maximum data. '''
    
    # Determine the number having in the data list
    n = len(data_list)
    
    # Check whether the data list is empty
    if n == 0:
        max_data = 0
    else:
        # Initialize a maximum value
        max_data = data_list[0]
        
        for data in data_list[1:]:
            if data > max_data:
                max_data = data
    
    return max_data


def get_min(data_list):
    ''' Take a data list and return its minimum data. '''
    
    # Determine the number having in the data list
    n = len(data_list)
    
    # Check whether the data list is empty
    if n == 0:
        min_data = 0
    else:
        # Initialize a minimum value
        min_data = data_list[0]
        
        for data in data_list[1:]:
            if data < min_data:
                min_data = data
    
    return min_data
    

def display_counts(data_list, categories, min, max):
    ''' Take a data list, categories, min and max values
        Display counts. '''
    
    # Determine the value between ranges
    category_size = (max - min) // categories
    
    # Determine the sorted data 
    sorted_data = sorted(data_list)
    
    # Initialize a positionition, a counting, and a sum counting
    position = 0
    count = 0
    sum_count = 0
    
    print('Frequency Distribution Table:')
    
    for data in sorted_data:
        # Check whether the data is out of the ranges
        if data < min or data > max:
            sorted_data.remove(data)
                
        else:
            again = True
        
            # Keep checking the data until it is in a range
            while again:
                # Determine the start and end of each range
                start = min + category_size * position
                end = start + category_size
                    
                # Check whether the next end is out of the range
                if end + category_size > max:
                    end = max + 1
                    
                # Check whether the data is in the range
                if data in range(start, end):
                    # Add up 1 to the counting if the data is in the range
                    count += 1
                    
                    again = False
                else:
                    # Display the range and its counting
                    print(f'{start}-{end - 1}: {count}')
                            
                    # Calculate the sum counting
                    sum_count += count
                    
                    # Determine the next position and the next counting
                    position += 1      
                    count = 0

    # Display the last range and its counting
    print(f'{start}-{end - 1}: {len(sorted_data) - sum_count}')
    

def main():
    ''' Define main function. '''
    
    # Prompt the user for a list of numbers separated by a comma
    input_prompt = 'Enter numbers separated by a comma: '
    data_list = [int(number) for number in input(input_prompt).split(',')]
    
    # data_list = [35, 37, 19, 45, 49, 68, 95, 7, 5, 82, 84]
    # sorted_data = [5, 7, 19, 35, 37, 45, 49, 68, 82, 84, 95]
    
    # Display the ranges and its counting
    display_counts(data_list, 5, 0, 100)
    print('-----------')
    display_counts(data_list, 4, get_min(data_list), get_max(data_list))
    
# Call main fucntion
main()