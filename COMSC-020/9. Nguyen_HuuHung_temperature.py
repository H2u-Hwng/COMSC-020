# Huu Hung Nguyen
# 09/12/2021
# Nguyen_HuuHung_temperature.py
# The program prompts the user for temperature in celsius or fahrenheit.
# It then convert them and displays the result.


# Prompt the user for temperature in celsius or fahrenheit
temperature = float(input('What is the temperature? '))
unit = input('What is the unit of the temperature? Celsius or Fahrenheit? ')

# Convert them and print the result
if unit in ['Celsius', 'celsius', '°C', 'C', 'c']:
    deg_f = temperature * 9 / 5 + 32
    print('{} degrees celsius is {} degrees cahrenheit.'.
          format(temperature, deg_f))
else:
    deg_c = (temperature - 32) * 5 / 9
    print('{} degrees fahrenheit is {} degrees celsius.'.
          format(temperature, deg_c))
