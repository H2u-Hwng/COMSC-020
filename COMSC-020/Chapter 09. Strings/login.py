# Huu Hung Nguyen
# 10/28/2021
# Nguyen_HuuHung_login.py
# Program prompts users for a first name, last name, and 7 digit ID.
# Program contains function generating the login name by concatenating
# first two characters of lowercase first name, first two characters of
# lowercase last name, and last three digits of 7 digit ID. 
# It then displays the login name.

# Concatenate three strings to generate login name
# Return login name
def get_login_name(first_name, last_name, id_number):
    string1 = first_name[:2].lower()
    string2 = last_name[:2].lower()
    string3 = id_number[-3:]
    
    # Generate login name
    login_name = string1 + string2 + string3
    
    return login_name


# Define main function
def main():
    
    # Prompt user for first name, last name, and digit ID
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')
    digit_id = input('Please enter a 7 digit id: ')
    
    # Obtain login name
    login_name = get_login_name(first_name, last_name, digit_id)
    
    # Display login name
    print(f'Your login is {login_name}.')
    
# Call main function
main()
