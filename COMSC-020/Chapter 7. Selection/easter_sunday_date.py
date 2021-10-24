# Constants for first year, last year, date of march, and special years
FIRST_YEAR = 1900
LAST_YEAR = 2099
DATE_OF_MARCH = 31
SPECIAL_YEARS = [1954, 1981, 2049, 2076]

# Prompt and return year 
def get_year():
    valid = False
    
    # Enter year until valid year is entered
    while not valid:
        year = int(input('Enter a year between 1900 to 2099, or 0 to finish: '))
        
        # Check if valid year is entered
        if year == 0 or year in range(FIRST_YEAR, LAST_YEAR + 1):
            valid = True
        else:
            print('ERROR...year out of range')
            print('Please enter a year that is in range. \n')
            
    return year


# Calculate and return easter sunday date
def calculate_easter_sunday(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
      
    easter_sunday = 22 + d + e
      
    return easter_sunday


# Display easter sunday date in form month day, year
def get_date(year, easter_sunday):
    if easter_sunday > DATE_OF_MARCH:
        print(f'The date is April {easter_sunday - DATE_OF_MARCH}, {year}. \n')
    else:
        print(f'The date is March {easter_sunday}, {year}. \n')
        

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
            
            # Obtain easter sunday date
            easter_sunday = calculate_easter_sunday(year)
            
            # Check if year is in special years
            if year in SPECIAL_YEARS:
                easter_sunday -= 7
            
            # Display easter sunday date in form month day, year
            get_date(year, easter_sunday)
            
# Call main function
main()
