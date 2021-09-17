# Huu Hung Nguyen
# 09/16/2021
# Nguyen_HuuHung_house.py


# Library
import turtle

# Creat window
wn = turtle.Screen()

# Draw house
house = turtle.Turtle()
for n in range(4):
    house.forward(150)
    house.right(90)
for n in range(3):
    house.forward(150)
    house.left(120)
    
    
# Close window
wn.exitonclick()