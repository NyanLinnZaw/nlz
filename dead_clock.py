from turtle import *
from datetime import datetime
import time

speed(0)
pencolor("black")
pensize(3)
circle(80)

left(90)
penup()
goto(0,80)
pendown()
pencolor("red")
circle(1)
penup()
pencolor("black")
for i in range (12):
    pensize(2)
    forward(65)
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


second_angle = current_time.second
right(second_angle)
pendown()
forward(65)
penup()
home()
left(90)
goto(0,80)

    
    

hideturtle()
done()

    




