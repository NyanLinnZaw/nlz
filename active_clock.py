from turtle import *
from datetime import datetime
import time

window = Screen()
window.tracer(0)
hideturtle()


def clock():
    speed(0)
    pencolor("black")
    pensize(3)
    circle(80)
    penup()
    goto(0,80)
    fillcolor("red")
    begin_fill()
    circle(2)
    end_fill()
    left(90)
    pendown()
    for i in range(12):
        penup()
        forward(60)
        pendown()
        forward(10)
        penup()
        goto(0,80)
        right(30)

    current_time = datetime.now().time()
    hour_angle = 0.5 * ((current_time.hour * 60) + current_time.minute)
    right(hour_angle)
    pendown()
    forward(40)
    penup()
    home()
    left(90)
    goto(0,80)

    minute_angle = 6 * current_time.minute
    right(minute_angle)
    pendown()
    forward(60)
    penup()
    home()
    left(90)
    goto(0,80)

    second_angle = 6 * current_time.second
    right(second_angle)
    pendown()
    pencolor("red")
    forward(65)
    penup()
    home()
    pendown()

while True:
    clock()

    window.update()
    time.sleep(1)
    clear()

window.mianloop()




