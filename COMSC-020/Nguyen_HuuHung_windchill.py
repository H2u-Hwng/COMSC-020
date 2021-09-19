# Huu Hung Nguyen
# 09/19/2021
# Nguyen_HuuHung_windchill.py
# The program prompts the user for the temperature in Celsius,
# and the wind velocity in kilometers per hour.
# It then calculates the wind chill temperature and prints the result.


# Prompt user for temperature in Celsius
t = float(input('Enter temperature in degrees Celsius: '))

# Prompt user for wind velocity in kilometers per hour
v = float(input('Enter wind velocity in kilometers/hour: '))

# Calculate wind chill temperature
t_wc = 13.12 + (0.6215 * t) - (11.37 * v**0.16) + (0.3965 * t * v**0.16)

# Print result
print('The wind chill temperature in degrees Celsius is {:.3f}.'.
      format(t_wc))