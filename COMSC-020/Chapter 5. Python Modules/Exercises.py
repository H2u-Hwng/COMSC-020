# Huu Hung Nguyen
# 09/25/2021
# Nguyen_HuuHung_57Exercises.py
# Do 16, 17, 18.

# Import library
import random
import math

# 16
for n in range(1, 11):
    print(f'Random number {n:2}: {random.random()}')
    
# 17
for n in range(1, 11):
    print(f'Random number {n:2} in [25, 35]: {random.randrange(25, 36)}')
    
# 18
side1 = 3
side2 = 4
hypotenuse = math.hypot(side1, side2)
print(f'The length of the hypotenuse of a right triangle is {hypotenuse}.')

