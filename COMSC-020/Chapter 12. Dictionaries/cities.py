# Huu Hung Nguyen
# 12/02/2021
# Nguyen_HuuHung_cities.py
# The program opens a file named cities.txt.
# It creates a dictionary where the key is the city name and the value is
# a list that contains the country and population.
# It prints the total number of cities and the average population.
# It then prints the city name, country name, and population until the users
# press ENTER to quit.

# Constant for the input file
INPUT_FILE = 'cities.txt'

def capitalize_city(city):
    ''' Take a name of a city and capitalize each word in the name
        Return the result. '''
    
#    formated_city = city.title()
    
    # Initialize a formated city
    formated_city = ''
    
    for word in city.strip().split():
        formated_city += word.capitalize() + ' '
        
    formated_city = formated_city.strip()
    
    return formated_city


def get_mean(data_list):
    ''' Take a data list and calculate its mean
        Return the mean of the data list. '''
    
    # Determine the numbers in the data list
    n = len(data_list)
    
    # Check whether the numbers is not 0
    if n > 0:
        # Calculate the mean of the data list
        mean = sum(data_list) / n
    else:
        mean = 0
        
    return mean


def create_dict(input_file):
    ''' Take a file and create a dictionary with its information
        Retunr the dictionary. '''
    
    # Open file
    open_file = open(input_file, 'r')
    
    # Initialize an empty dicitonary
    cities_dict = {}
    
    # Read each line in the input file
    for line in open_file:
        # Strip whitespace off and split city and its information
        city_info = line.strip().split(',')
        
        # Determine city, country, and population in the file
        city = city_info[0]
        country = city_info[1]
        population = int(city_info[2])
        
        # Add city, country, and population to the cities dictionary
        cities_dict[city] = [country, population]
    
    # Close file
    open_file.close()
    
    return cities_dict


def main():
    ''' Define main function. '''
    
    # Determine the cities dictionary
    cities_dict = create_dict(INPUT_FILE)
    
    # Initialize a populations list
    populations = []

    for city_info in cities_dict.values():
        # Add the population to the end of the populations list
        populations.append(city_info[1])
        
    # Determine and display the number of cities
    total_cities = len(cities_dict)
    print('Number of cities:', total_cities)
    
    # Determine and display the mean population
    mean_population = get_mean(populations)
    print(f'Average population: {int(mean_population):,} \n')
    
    again = True
    
    # Repeatedly ask the users until they press ENTER
    while again:
        # Prompt the user for a city 
        city = input('Enter a city, or just ENTER to quit: ')
        
        # Check whether the city is empty
        if city == '':
            again = False
        else:
            # Determine the city after formated 
            city = capitalize_city(city)
            
            # Check whether the city is in the cities dictionary
            try:
                country, population = cities_dict.get(city)
                print('{} is in {} and has a population of {:,}. \n'.format(city, country, population))
            except:
                print(city, 'is not in the list, sorry. \n')
    
# Call main function
main()
