# Huu Hung Nguyen
# 09/19/2021
# windchill.py
# The program prompts the user for the temperature in Celsius,
# and the wind velocity in kilometers per hour.
# It then calculates the wind chill temperature and prints the result.

# Prompt user for temperature in Celsius
temp = float(input('Enter temperature in degrees Celsius: '))

# Prompt user for wind velocity in kilometers per hour
wind_velocity = float(input('Enter wind velocity in kilometers/hour: '))

# Calculate wind chill temperature
wind_chill_temp = 13.12 + (0.6215 * temp) - (11.37 * wind_velocity**0.16) + (0.3965 * temp * wind_velocity**0.16)

# Print result
print(f'The wind chill temperature in degrees Celsius is {wind_chill_temp:.3f}.')
