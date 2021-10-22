# Huu Hung Nguyen
# 10/20/2021
# Nguyen_HuuHung_payroll.py
# Constants for regular hours and overtime rate.
# Program prompts user for hours and hourly rate.
# It then calculates and displays the total wages for the week.

# Constants for regular hours and overtime rate
REGULAR_HOURS = 40
OVERTIME_RATE = 1.5

# Take hours and hourly rate, calculate and return total wages for the week
def wages(hrs, hr_rate):
    
    # Calculate total wages for the week5
    if hrs <= REGULAR_HOURS:
        total_wages = hrs * hr_rate
    else:
        total_wages = REGULAR_HOURS * hr_rate + \
                (hrs - REGULAR_HOURS) * OVERTIME_RATE * hr_rate
    
    return total_wages


# Define main function
def main():
    
    # Prompt user for hours and hourly rate
    hours = float(input('Enter the number of hours worked in the week: '))
    hourly_rate = float(input('Enter the hourly rate: '))
    
    # Obtain total wages
    total_wages = wages(hours, hourly_rate)
    
    # Display result
    print(f'Total wages for the week: ${total_wages:,.2f}')
    
# Call main function
main()