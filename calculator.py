from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression +str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

window = Tk()
window.configure(bg="light green")

equation = StringVar()

e1 = Entry(window,textvariable=equation)
e1.grid(row=0,columnspan=8,ipadx=70,sticky=W)

b1 = Button(window,text="1",fg="black",bg="red",command=lambda:press(1),width=7,height=1)
b1.grid(row=1,column=0)
b2 = Button(window,text="2",fg="black",bg="red",command=lambda:press(2),width=7,height=1)
b2.grid(row=1,column=1)
b3 = Button(window,text="3",fg="black",bg="red",command=lambda:press(3),width=7,height=1)
b3.grid(row=1,column=2)
b4 = Button(window,text="+",fg="black",bg="red",command=lambda:press("+"),width=7,height=1)
b4.grid(row=1,column=3)

b5 = Button(window,text="4",fg="black",bg="red",command=lambda:press(4),width=7,height=1)
b5.grid(row=2,column=0)
b6 = Button(window,text="5",fg="black",bg="red",command=lambda:press(5),width=7,height=1)
b6.grid(row=2,column=1)
b7 = Button(window,text="6",fg="black",bg="red",command=lambda:press(6),width=7,height=1)
b7.grid(row=2,column=2)
b8 = Button(window,text="-",fg="black",bg="red",command=lambda:press("-"),width=7,height=1)
b8.grid(row=2,column=3)

b9 = Button(window,text="7",fg="black",bg="red",command=lambda:press(7),width=7,height=1)
b9.grid(row=3,column=0)
b10 = Button(window,text="8",fg="black",bg="red",command=lambda:press(8),width=7,height=1)
b10.grid(row=3,column=1)
b11 = Button(window,text="9",fg="black",bg="red",command=lambda:press(9),width=7,height=1)
b11.grid(row=3,column=2)
b12 = Button(window,text="*",fg="black",bg="red",command=lambda:press("*"),width=7,height=1)
b12.grid(row=3,column=3)

b13 = Button(window,text="0",fg="black",bg="red",command=lambda:press(0),width=7,height=1)
b13.grid(row=4,column=0)
b14 = Button(window,text="Clear",fg="black",bg="red",command=clear,width=7,height=1)
b14.grid(row=4,column=1)
b15 = Button(window,text="=",fg="black",bg="red",command=equalpress,width=7,height=1)
b15.grid(row=4,column=2)
b16 = Button(window,text="/",fg="black",bg="red",command=lambda:press("/"),width=7,height=1)
b16.grid(row=4,column=3)

b17 = Button(window,text=".",fg="black",bg="red",command=lambda:press("."),width=7,height=1)
b17.grid(row=5,column=0)

window.mainloop()




