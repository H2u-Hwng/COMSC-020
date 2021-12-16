# Huu Hung Nguyen
# 09/17/2021
# days.py
# The program prompts the user for the starting day
# and the length of staying day.
# It the calculates the numeber of day of the week returning
# and prints the result.

# Prompt user for starting day
starting_day = int(input('Enter the starting day in 0 (a Sunday) - 6 (a Saturday): '))

# Prompt user for length of staying day
staying_day = int(input('Enter the length of staying day: '))

# Calculate number of day of week returning in 0 (a Sunday) - 6 (a Saturday)
returning_day = (starting_day + staying_day) % 7

# Print result
print('The number of day of the week I will return on is {}.'.format(returning_day))
