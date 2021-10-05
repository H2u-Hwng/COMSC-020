# The program prompts the user for the string
# It then changes "space" between words in string to "-",
# and displays the new string with "-".

# Prompt user for string
string = input('Enter the string: ')

# Change "space" to "-"
result = '-'.join(string.split(' '))

# Display new string with "-"
print(f'The string "{string}" is transfromed into "{result}"')