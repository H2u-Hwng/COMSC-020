# https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/Exercises.html
# Q7

# Library
import turtle

# Create window
wn = turtle.Screen()

# Create turtle named pirate
pirate = turtle.Turtle()

# Draw path taken by drunk pirate
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(angle)
    pirate.forward(100)

# Display msg
print(f"The pirate's final heading was {pirate.heading()}.")

# Close window
wn.exitonclick()