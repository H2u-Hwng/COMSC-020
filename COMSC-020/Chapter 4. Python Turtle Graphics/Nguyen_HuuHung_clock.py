# Huu Hung Nguyen
# 09/18/2021
# Nguyen_HuuHung_clock.py
# Draw a clock.

# Library
import turtle

# Open window
wn = turtle.Screen()
wn.bgcolor('lightgreen')

# Draw clock
clock = turtle.Turtle()
clock.shape('turtle')
clock.up()
clock.color('blue')
clock.pensize(3)
for i in range(12):
    clock.forward(117)
    clock.down()
    clock.forward(10)
    clock.up()
    clock.forward(20)
    clock.stamp()
    clock.goto(0, 0)
    clock.right(360 / 12)
    
# Close window
wn.exitonclick()
