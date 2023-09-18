from turtle import *
from datetime import datetime
import time

screen = Screen()
screen.tracer(0)

def draw_clock():
    speed(0)
    penup()
    goto(0,-200)
    pendown()
    pensize(3)
    pencolor('darkgray')
    for i in range(60):
        circle(200,6)
        left(90)
        forward(10)
        backward(10)
        right(90)

    pencolor("black")
    for i in range(12):
        circle(200,30)
        left(90)
        forward(20)
        backward(20)
        right(90)

def draw_hand():
    penup()
    goto(0,0)
    
    #hour
    left(90)
    current_time = datetime.now().time()
    hour_angle = 0.5 * ((current_time.hour * 60) + current_time.minute)
    right(hour_angle)
    penup()
    pensize(2)
    pencolor("gray")
    fillcolor("gray")
    begin_fill()
    forward(150)
    left(150)
    pendown()
    forward(20)
    home()
    left(90)
    right(hour_angle)
    penup()
    forward(150)
    right(150)
    pendown()
    forward(20)
    home()
    end_fill()
    
    #minute
    left(90)
    minute_angle = 6 * current_time.minute
    right(minute_angle)
    penup()
    pensize(2)
    pencolor("black")
    fillcolor("black")
    begin_fill()
    forward(180)
    left(150)
    pendown()
    forward(20)
    home()
    left(90)
    right(minute_angle)
    penup()
    forward(180)
    right(150)
    pendown()
    forward(20)
    home()
    end_fill()

    #second
    left(90)
    second_angle = 6 * current_time.second
    right(second_angle)
    penup()
    pensize(2)
    pencolor("red")
    fillcolor("red")
    begin_fill()
    forward(180)
    left(150)
    pendown()
    forward(10)
    home()
    left(90)
    right(second_angle)
    penup()
    forward(180)
    right(150)
    pendown()
    forward(10)
    home()
    end_fill()

while True:
    draw_clock()
    draw_hand()

    screen.update()
    time.sleep(1)
    clear()
    
    
    
    

 
    
    


