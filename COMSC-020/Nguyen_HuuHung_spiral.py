# Huu Hung Nguyen
# 09/20/2021
# Nguyen_HuuHung_spiral.py
# The program assumes the first length is 10.
# It prompts the user for the number of sides,
# the number of lines to draw, and the percentage of increase length.
# It then draws polygonal spirals.


# Library
import turtle

# Open window
wn = turtle.Screen()

# Assume first length is 10
LENGTH = 10

# Draw polygonal spirals
figure = turtle.Turtle()
figure.pensize(2)
# figure.speed(0)
num_sides = int(input('Enter the number of sides of the polygon: '))
iterations = int(input('How many times to spiral? '))
increase_length_rate = (float(input('What is the percentage of \
increase length? '))) / 100
for n in range(iterations):
    figure.fd(LENGTH)
    figure.rt(360 / num_sides)
    LENGTH *= (1 + increase_length_rate)
    
# Close window
wn.exitonclick()