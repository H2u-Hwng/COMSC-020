# Huu Hung Nguyen
# 11/15/2021
# Nguyen_HuuHung_density.py
# The program reads file named "density.txt".
# It then determine and displays minimum density, maximum density,
# average density, and median density.

# Constant for input file
INPUT_FILE = 'density.txt'

def is_even(n):
    '''Return True if the paramerter n is even and False otherwise.'''
    
    if n % 2 == 0:
        even = True
    else:
        even = False
    
    return even


def get_median(data_list):
    '''Take a list of numbers and return the median.'''
    
    # Determine sorted data list
    sorted_data_list = sorted(data_list)
    
    # Determine how many numbers in the list
    n = len(data_list)
    
    # Determine the median
    if is_even(n):
        median = (sorted_data_list[(n // 2)] + \
                  sorted_data_list[(n // 2) - 1]) / 2.0
    else:
        median = sorted_data_list[(n - 1) // 2] 
    
    return median


def get_mean(data_list):
    '''Take a list of numbers and return the mean.'''
    
    # Determine how many numbers in the list
    n = len(data_list)
    
    # Add up the numbers in the list
    sum_data = sum(data_list)
    
    # Calculate the mean
    mean = sum_data / n
    
    return mean


def sorter(data_list):
    '''Create and return a key for the data list.'''
    
    key = data_list[1]
    
    return key


def main():
    '''Define main function.'''
    
    # Open file and automatically close it when being done
    with open(INPUT_FILE, 'r') as input_file:
    
        # Initialize the lists for planets densities, planets, and densities
        planets_densities = []
        planets = []
        densities = []
        
        # Creat a list of planets densities
        for line in input_file:
            # Strip whitespace off the end and split planet and density
            planet_density = line.strip().split()
            
            # Add planet and density to the end of the planets densities list
            planets_densities.append(planet_density)
        
        # Determine sorted planets densities list
        sorted_planets_densities = sorted(planets_densities, key = sorter)
        
        # Create lists of planets and densities
        for element in sorted_planets_densities:
            # Add the planet to the end of the planets list
            planets.append(element[0])
            
            # Add the density to the end of the densities list
            densities.append(float(element[1]))
        
        # Determine and display the minumum and maximum densities
        print(f'{planets[0]} has the minimum density of {densities[0]}.')
        print(f'{planets[-1]} has the maxiimum density of {densities[-1]}.')
        
        # Determine and display the mean density
        mean_density = get_mean(densities)
        print(f'The mean density is {mean_density:.3f}.')
        
        # Determine and display the median density
        median_density = get_median(densities)
        print(f'The median density is {median_density:.3f}.')

# Call main function
main()