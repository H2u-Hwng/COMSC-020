# The promgram prompts the user for one number.
# It then displays the n*n times table.

# Prompt user for one number
num = int(input('Enter the number for the n*n times table: '))


# Display n*n times table
for a in range(1, num + 1):
    for b in range(1, num + 1):
        print(f'{b} x {a} = {b * a}', end = ' ')
        if b == a:
            print('')
            break
    