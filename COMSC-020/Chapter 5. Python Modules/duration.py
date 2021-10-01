# Huu Hung Nguyen
# 09/30/2021
# duration.py
# The program prompt the users for the starting hour, the starting minute,
# the ending hour, and the ending minute.
# It then calculate and displays the duration. 

# Prompt user for starting hour and starting minute
start_hr = int(input('Enter starting hour: '))
start_min = int(input('Enter starting minute: '))

# Prompt user for ending hour and ending minute
end_hr = int(input('Enter ending hour: '))
end_min = int(input('Enter ending minute: '))

# Calculate duration 
duration = (end_hr * 60 + end_min) - (start_hr * 60 + start_min)
duration_hr = duration // 60
duration_min = duration % 60

# Display duration 
print(f'Duration is {duration_hr} hours and {duration_min} minutes.')