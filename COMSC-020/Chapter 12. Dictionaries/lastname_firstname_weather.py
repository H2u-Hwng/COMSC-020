FILE_NAME = 'weather.txt'

def get_mean(data_list):
    ''' Take a data list and return its mean. '''
    
    # Determine the number having in the data list
    n = len(data_list)
    
    # Check whether the number is 0
    if n == 0:
        mean = 0
    else:
        mean = sum(data_list) / n
    return mean
def create_dict(file_name):
    ''' Open file and return the file handle object. '''
    
    input_file = open(file_name, 'r')
    
    # Initialize an empty dictionary
    weather_dict = {}
    
    # Create the weather dictionary
    for line in input_file:
        items = line.strip().split(';')
        date = items[0]
        day_of_week = items[1]
        high_temp = float(items[2])
        low_temp = float(items[3])
        weather_dict[date] = [day_of_week, high_temp, low_temp]
    
    input_file.close()
    
    return weather_dict


def main():
    ''' Define main function. '''
    
    # Determine the weather data dictionary
    weather_dict = create_dict(FILE_NAME)
    
    # Determine and display the number of date in weather dictionary
    n_entries = len(weather_dict)
    print(f'# of entries in dictionary: {n_entries}')
    
    # Initialize the max temps list and min temps list
    high_temps_list = []
    low_temps_list = []
    
    # Check each weather information in the values of the dictionary
    for a_value in weather_dict.values():
        # Add the high_temp temperature to the end of the max temps list
        high_temps_list.append(a_value[1])
        
        # Add the low_temp temperature to the end of the min temps list
        low_temps_list.append(a_value[2])
    
    # Determine and display the mean of min temperatures
    mean_low_temps = get_mean(low_temps_list)
    print(f'Average low temperature is {mean_low_temps:.1f}\u00b0C')
    
    # Determine and display the mean of max temperatures
    mean_high_temps = get_mean(high_temps_list)
    print(f'Average high temperature is {mean_high_temps:.1f}\u00b0C')
    
    print() # for readability
    
    
    
    # Keep asking the users until they press ENTER
    again = True
    while again:
        # Prompt the user for the date
        input_date = input('Enter date in form yyyy-mm-dd: ')
        
        # Check whether the date is empty
        if input_date == '':
            again = False
        else:
            # Check whether the date is in the weather data dictionary
            try:
                info = weather_dict.get(input_date)
                
                # Display the date, its day_of_week, low_temp and high_temp temperatures
                print(f'{input_date} ({info[0]})', \
                      f'Low {info[2]}\u00b0C', \
                      f'High {info[1]}\u00b0C')
            except:
                print(input_date, 'is not in the weather data.')
            print() # for readability
            
# Call main function
main()

# low_total = 0.0
# for a_key in weather_dict.keys():
#     low_total += weather_dict[a_key][2]