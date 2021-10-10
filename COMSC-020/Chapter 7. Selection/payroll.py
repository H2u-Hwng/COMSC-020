# Constants
REGULAR_HOURS = 40
OVERTIME_RATE = 1.5

# Define wages function
def wages(hours, hourly_rate):
    
    # Calculate total wages for the week
    if hours <= REGULAR_HOURS:
        total_wages = hourly_rate * hours 
    else:
        overtime = hours - REGULAR_HOURS
        total_wages = hourly_rate * (REGULAR_HOURS + OVERTIME_RATE * overtime)
        
    return total_wages

# Define main function
def main():
    
    # Prompt user for hours worked and hourly rate
    hours = float(input('Enter the number of hours worked: '))
    hourly_rate = float(input('Enter the hourly rate: '))
    
    # Get total wages
    total_wages = wages(hours, hourly_rate)
    
    # Display total wages
    print(f'The total wages is ${total_wages:,.2f}')
    
# Call main function
main()