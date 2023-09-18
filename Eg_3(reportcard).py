from tkinter import *

def Submit():
    total = 0
    if e4.get() == 'A':
        e4_var.set(40)
        total += 40
    if e4.get() == 'B':
        e4_var.set(36)
        total += 36
    if e4.get() == 'C':
        e4_var.set(32)
        total += 32
    if e4.get() == 'D':
        e4_var.set(24)
        total += 24
    if e4.get() == 'P':
        e4_var.set(28)
        total += 28
    if e4.get() == 'F':
        e4_var.set(0)
        total += 0
    if e4.get() == 'G':
        e4_var.set(0)
        total += 0
        
    if str(e5.get()) == 'A':
        e5_var.set(40)
        total += 40
    if str(e5.get()) == 'B':
        e5_var.set(36)
        total += 36
    if str(e5.get()) == 'C':
        e5_var.set(32)
        total += 32
    if str(e5.get()) == 'D':
        e5_var.set(24)
        total += 24
    if str(e5.get()) == 'P':
        e5_var.set(28)
        total += 28
    if str(e5.get()) == 'F':
        e5_var.set(0)
        total += 0
    if str(e5.get()) == 'G':
        e5_var.set(0)
        total += 0

    if str(e6.get()) == 'A':
        e6_var.set(40)
        total += 40
    if str(e6.get()) == 'B':
        e6_var.set(36)
        total += 36
    if str(e6.get()) == 'C':
        e6_var.set(32)
        total += 32
    if str(e6.get()) == 'D':
        e6_var.set(24)
        total += 24
    if str(e6.get()) == 'P':
        e6_var.set(28)
        total += 28
    if str(e6.get()) == 'F':
        e6_var.set(0)
        total += 0
    if str(e6.get()) == 'G':
        e6_var.set(0)
        total += 0

    if str(e7.get()) == 'A':
        e7_var.set(40)
        total += 40
    if str(e7.get()) == 'B':
        e7_var.set(36)
        total += 36
    if str(e7.get()) == 'C':
        e7_var.set(32)
        total += 32
    if str(e7.get()) == 'D':
        e7_var.set(24)
        total += 24
    if str(e7.get()) == 'P':
        e7_var.set(28)
        total += 28
    if str(e7.get()) == 'F':
        e7_var.set(0)
        total += 0
    if str(e7.get()) == 'G':
        e7_var.set(0)
        total += 0

    final_total.set(total)
    sgpa.set(total/15)

    
window = Tk()
window.title("Report Card")
window.geometry("700x250")

Label(window,text="Name").grid(row=0,column=0)
e1 = Entry(window).grid(row=0,column=1)
Label(window,text="Roll.No").grid(row=1,column=0)
e2 = Entry(window).grid(row=1,column=1)
Label(window,text="Reg.No").grid(row=0,column=3)
e3 = Entry(window).grid(row=0,column=4)

Label(window,text="Sirl.No").grid(row=2,column=0)
Label(window,text="Subject").grid(row=2,column=1)
Label(window,text="Grade").grid(row=2,column=2)
Label(window,text="Sub Credit").grid(row=2,column=3)
Label(window,text="Credit obtained").grid(row=2,column=4)

No_list = [1,2,3,4]
row = 3
for i in No_list:
    Label(window,text=i).grid(row=row,column=0)
    row += 1

Sub_list = ["CS 201","CS 202","MA 201","EC 201"]
row = 3
for i in Sub_list:
    Label(window,text=i).grid(row=row,column=1)
    row += 1

e4 = Entry(window)
e4.grid(row=3,column=2)
e5 = Entry(window)
e5.grid(row=4,column=2)
e6 = Entry(window)
e6.grid(row=5,column=2)
e7 = Entry(window)
e7.grid(row=6,column=2)

Credit_list = [4,4,3,4]
row = 3
for i in Credit_list:
    Label(window,text=i).grid(row=row,column=3)
    row += 1

e4_var = StringVar()
Label(window,textvariable=e4_var).grid(row=3,column=4)
e5_var = StringVar()
Label(window,textvariable=e5_var).grid(row=4,column=4)
e6_var = StringVar()
Label(window,textvariable=e6_var).grid(row=5,column=4)
e7_var = StringVar()
Label(window,textvariable=e7_var).grid(row=6,column=4)

Label(window,text="Total credit").grid(row=7,column=3)
final_total = StringVar()
Label(window,textvariable=final_total).grid(row=7,column=4)
Label(window,text="SGPA").grid(row=8,column=3)
sgpa = StringVar()
Label(window,textvariable=sgpa).grid(row=8,column=4)


Button(window,text="Submit",bg="blue",fg="black",command=Submit).grid(row=8,column=1)

window.mainloop()
