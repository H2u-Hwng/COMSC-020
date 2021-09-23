# Huu Hung Nguyen
# 09/16/2021
# Nguyen_HuuHung_house.py
# The program draws the house.

# Library
import turtle

# Create window
wn = turtle.Screen()

# Create turtle named house
house = turtle.Turtle()

# Draw square
for n in range(4):
    house.forward(150)
    house.right(360 / 4)
    
# Draw triangle
for n in range(3):
    house.forward(150)
    house.left(360 / 3)
    
# Exit window
wn.exitonclick()