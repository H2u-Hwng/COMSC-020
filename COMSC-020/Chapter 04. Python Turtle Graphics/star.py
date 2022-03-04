# Huu Hung Nguyen
# 09/19/2021
# Nguyen_HuuHung_star.py
# Draw a star.

# Library
import turtle

# Create window
wn = turtle.Screen()

# Create turtle named star
star = turtle.Turtle()
star.pensize(4)
star.hideturtle()

# Draw star
for n in range(5):
    star.forward(155)
    star.right(144)

# Close window
wn.exitonclick()
