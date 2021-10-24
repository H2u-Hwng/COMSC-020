# Prompt and return year
def get_year():
    valid = False
    
    # Enter year until valid year is entered
    while not valid:
        year = int(input('Enter a year, or 0 to finish: '))
        
        # Check if valid year is entered
        if year >= 0:
            valid = True
        else:
            print('Please enter a valid year! \n')
            
    return year


# Display leap year or otherwise
def get_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print(f'{year} is a leap year. \n')
    elif year % 400 == 0:
        print(f'{year} is a leap year. \n')
    else:
        print(f'{year} is not a leap year. \n')


# Define main function
def main():
    finish = False
    
    # Enter year until user enters 0
    while not finish:
        
        # Obtain year
        year = get_year()
        
        # Check if user finishes entering year
        if year == 0:
            finish = True
        else:
            
            # Display leap year or otherwise
            get_leap_year(year)
            
# Call main function    
main()
