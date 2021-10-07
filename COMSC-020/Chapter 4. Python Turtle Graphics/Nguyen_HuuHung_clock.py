# Huu Hung Nguyen
# 09/18/2021
# Nguyen_HuuHung_clock.py
# Draw a clock.

# Library
import turtle

# Create window
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.setup(width = 500, height = 500)

# Create turtle named clock
clock = turtle.Turtle()
clock.shape('turtle')
clock.up()
clock.color('blue')
clock.pensize(3)
clock.speed(0)

# Calculate angle
angle = 360 / 12

# Draw clock
for i in range(12):
    clock.forward(117)
    clock.down()
    clock.forward(10)
    clock.up()
    clock.forward(20)
    clock.stamp()
    clock.forward(-147)
    clock.right(angle)
    
# Close window
wn.exitonclick()
