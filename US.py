import turtle as t 
t.speed(0)

x = 0
y = 0

def red_rectangle():
    for i in range(2):
        t.pencolor("red")
        t.fillcolor("red")
        t.begin_fill()
        t.forward(300)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.end_fill()

for i in range(7):
    y = y - 25
    red_rectangle()
    t.penup()
    t.goto(0,y)

t.goto(0,0)

def blue_rectangle():
    for i in range(2):
        t.fillcolor("blue")
        t.begin_fill()
        t.forward(130)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.end_fill()

blue_rectangle()

def star():
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    for i in range(5):
        t.forward(10)
        t.right(144)
    t.end_fill()

y = 0
y = y - 10
t.goto(0,y)
t.penup()
t.forward(10)
t.pendown()

def sixstar_row():
    for i in range(6):
        star()
        t.penup()
        t.forward(20)
        t.pendown()

for i in range(5):
    y = y - 20
    sixstar_row()
    t.penup()
    t.goto(10,y)
    t.pendown()

t.penup()
t.goto(20,-20)
t.pendown()

def fivestar_row():
    for i in range(5):
        star()
        t.penup()
        t.forward(20)
        t.pendown()

y = -20
for i in range(4):
    y = y - 20
    fivestar_row()
    t.penup()
    t.goto(20,y)
    t.pendown()
    
t.hideturtle()
t.done()
