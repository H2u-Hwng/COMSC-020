# Huu Hung Nguyen
# 09/18/2021
# Nguyen_HuuHung_clock.py
# Draw a clock.


# Library
import turtle

# Create a screen
wn = turtle.Screen()

# Draw a clock
clock = turtle.Turtle()
clock.shape('turtle')
clock.stamp()
clock.hideturtle()
clock.penup()
for i in range(12):
    clock.forward(117)
    clock.pendown()
    clock.forward(10)
    clock.penup()
    clock.forward(20)
    clock.stamp()
    clock.backward(147)
    clock.right(360 / 12)
    
# Exit screen on click
wn.exitonclick()