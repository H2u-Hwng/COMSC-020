# Prompt user for loan amount, yearly interest rate as a decimal, and
# the number of years.
# Calculate and display the interest.

# Calculate and return interest
def get_interest(loan_amount, years_percent, years):
    
    # Calculate interest
    interest = loan_amount * (years_percent / 100) * years
    
    return interest


# Define the main function
def main():
    
    # Prompt user for principal, annual_percent, years
    principal = float(input('What is the amount of the loan? $'))
    annual_percent = \
            float(input('What is the annual interest rate as a percent? '))
    years = float(input('How many years will the loan be for? '))
    
    # Obtain interest
    interest = get_interest(principal, annual_percent, years)
    
    # Display interest
    print(f'The simple interest will be ${interest:,.2f}')

# Call the main function
main()