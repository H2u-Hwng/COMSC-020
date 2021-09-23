# Huu Hung Nguyen
# 09/22/2021
# Nguyen_HuuHung_spiral.py
# The program assumes the first length is 10.
# It prompts the user for the number of sides, the interations, 
# and the percentage of increase length.
# It then draws polygonal spirals.

# Library
import turtle

# Assume first length is 10
LENGTH = 10

# Create window
wn = turtle.Screen()

# Create turtle named figure
figure = turtle.Turtle()
figure.pensize(2)
figure.speed(0)

# Assign first length side
length_side = LENGTH

# Prompt user for number of sides and iterations
num_sides = int(input('Enter the number of sides: '))
iterations = int(input('Enter the number of lines to draw: '))

# Prompt user for percent of increase length and calculate rate
increase_percent = float(input('What is the percentage of increase length? '))
increase_rate = increase_percent / 100

# Calculate angle
angle = 360 / num_sides

# Draw polygonal spiral
for n in range(iterations):
    figure.forward(length_side)
    figure.right(angle)
    
    increase_side = length_side * increase_rate
    length_side += increase_side

# Exit window
wn.exitonclick()