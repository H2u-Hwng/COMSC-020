# Huu Hung Nguyen
# 09/15/2021
# temperature.py
# The program prompts the user for temperature in celsius or fahrenheit.
# It then convert them and displays the result.

# Prompt the user for temperature in celsius or fahrenheit
temperature = float(input('What is the temperature? '))
unit = input('What is the unit of the temperature? \
Celsius or Fahrenheit? ')

# Convert them and print the result
if unit in ['Celsius', 'celsius', '°C', 'C', 'c']:
    deg_f = temperature * 9 / 5 + 32
    print('{:.3f} degrees celsius is {:.3f} degrees cahrenheit.'.
          format(temperature, deg_f))
    
    # Print msg
    if deg_f < 50:
        print('Bruh, you should wear a coat!')
    elif deg_f > 85:
        print("It's super hot out! Be sure to drink extra water.")
    else:
        print("Yeah, it's nice weather!")

else:
    deg_c = (temperature - 32) * 5 / 9
    print('{:.3f} degrees fahrenheit is {:.3f} degrees celsius.'.
          format(temperature, deg_c))
