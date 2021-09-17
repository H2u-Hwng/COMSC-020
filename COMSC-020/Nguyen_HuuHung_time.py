# Huu Hung Nguyen
# 09/16/2021
# Nguyen_HuuHung_time.py
# The program promt the user for the current time and the waiting time.
# It then calculates the time after waiting and prints the result.


# Prompt user for current time
current_time = int(input('Enter the current time in hours 0 - 23: '))

# Prompt user for waiting time
waiting_time = int(input('Enter the waiting time: '))

# Calculate time after waiting in hours 0 - 23
time_after_waiting = (current_time + waiting_time) % 24

# Print result
print('The time will be on the clock when the alarm goes off is {}.'.
      format(time_after_waiting))