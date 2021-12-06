# Huu Hung Nguyen
# 11/19/2021
# Nguyen_HuuHung_density.py
# The program reads file named "density.txt".
# It then determine and displays minimum density, maximum density,
# average density, and median density.

# Constant for input file
INPUT_FILE = 'density.txt'

def is_even(n):
    '''Return True if the paramerter n is even and False otherwise.'''
    
    even = n % 2 == 0
    
    return even


def get_median(data_list):
    '''Take a list of numbers and return the median.'''
    
    # Determine sorted data list
    sorted_data_list = sorted(data_list)
    
    # Determine how many numbers in the list
    n = len(data_list)
    
    # Determine the median
    if is_even(n):
        median = (sorted_data_list[(n // 2)] + sorted_data_list[(n // 2) - 1]) / 2.0
    else:
        median = sorted_data_list[(n - 1) // 2] 
    
    return median


def get_mean(data_list):
    '''Take a list of numbers and return the mean.'''
    
    # Determine how many numbers in the list
    n = len(data_list)
    
    # Check whether the data list is empty
    if n == 0:
        mean = 0
    else:
        # Calculate the mean
        mean =  sum(data_list) / n
    
    return mean


def get_maximum(data_list, names):
    '''Take the data list and the names list
       Return the maximum data and corresponding name.'''
    
    # Determine the maximum data
    max_data = max(data_list)
    
    # Determine corresponding name with the maximum data
    max_index = data_list.index(max_data)
    max_name = names[max_index]
    
    return max_data, max_name


def get_minimum(data_list, names):
    '''Take the data list and the names list
       Return the minimum data and corresponding name.'''
    
    # Determine the minimum data
    min_data = min(data_list)
    
    # Determine corresponding name with the minimum data
    min_index = data_list.index(min_data)
    min_name = names[min_index]
    
    return min_data, min_name


def main():
    '''Define main function.'''
    
    # Open file and automatically close it when being done
    with open(INPUT_FILE, 'r') as input_file:
    
        # Initialize the planets list and the densities list
        planets = []
        densities = []
        
        # Create the planets list and the densities list
        for line in input_file:
            # Strip whitespace off the end and split planet and density
            planet_density = line.strip().split()
            
            # Add the planet to the end of the planets list
            planets.append(planet_density[0])
            
            # Add the density to the end of the densities list
            densities.append(float(planet_density[1]))
        
        # Determine and display the minimum and maximum densities
        min_density, min_planet = get_minimum(densities, planets)
        print(f'{min_planet} has the minimum density of {min_density} kg/m3.')
        
        max_density, max_planet = get_maximum(densities, planets)
        print(f'{max_planet} has the maximum density of {max_density} kg/m3.')
        
        # Determine and display the mean density
        mean_density = get_mean(densities)
        print(f'The mean density is {mean_density:.3f}.')
        
        # Determine and display the median density
        median_density = get_median(densities)
        print(f'The median density is {median_density:.3f}.')

# Call main function
main()
