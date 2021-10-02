# Library
import turtle
import datetime

# Create window
wn = turtle.Screen()
wn.setup(width = 600, height = 600)
wn.tracer(0)

# Create turtle named clock
clock = turtle.Turtle()
clock.shape('square')
clock.hideturtle()
clock.pensize(4)
clock.color('black')
clock.speed(0)

def draw_clock(hr, min, sec, mic, clock):
    
    # Draw clock face
    clock.up()
    clock.goto(0, 150)
    clock.setheading(180)
    clock.down()
    clock.circle(150)
    
    # Draw lines for clock face
    clock.up()
    clock.goto(0, 0)
    angle = 360 / 12
    
    for n in range(1, 13):
        clock.rt(angle)
        clock.fd(150)
        clock.stamp()
        clock.fd(-150)
        
    clock.down()
    
    # Draw hour hand
    clock.goto(0, 0)
    clock.setheading(90)
    clock.rt(hr / 12 * 360 + min / 60 * 30)
    clock.fd(100)

    # Draw minute hand
    clock.goto(0, 0)
    clock.setheading(90)
    clock.rt(min / 60 * 360 + sec / 60 * 6)
    clock.fd(120)
    
    # Draw second hand
    turtle.hideturtle()
    turtle.pensize(2)
    turtle.color('red')
    
    turtle.goto(0, 0)
    turtle.setheading(90)
    turtle.rt(sec / 60 * 360 + mic / 10**6 * 6)
    turtle.fd(120)
    
# Create updating time clock
while True:
    hr = datetime.datetime.now().hour % 12
    min = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    mic = datetime.datetime.now().microsecond
    
    draw_clock(hr, min, sec, mic, clock)
    wn.update()
    clock.clear()
    turtle.clear()
    
# Close window
wn.done()