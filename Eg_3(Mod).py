from tkinter import *

def Submit():
    credit_dic = {
        "A" : 40,
        "B" : 36,
        "C" : 32,
        "D" : 24,
        "P" : 28,
        "F" : 0, 
        "G" : 0, }
    total = 0
    for key in credit_dic.keys():
        if str(e4.get()) == key:
            e4_value = credit_dic[key]
            Label(window,text=credit_dic[key]).grid(row=3,column=4)
        if str(e5.get()) == key:
            e5_value = credit_dic[key]
            Label(window,text=credit_dic[key]).grid(row=4,column=4)
        if str(e6.get()) == key:
            e6_value = credit_dic[key]
            Label(window,text=credit_dic[key]).grid(row=5,column=4)
        if str(e7.get()) == key:
            e7_value = credit_dic[key]
            Label(window,text=credit_dic[key]).grid(row=6,column=4)
    total = e4_value + e5_value + e6_value + e7_value
    Label(window,text=total).grid(row=7,column=4)
    spga = total / 15
    Label(window,text=spga).grid(row=8,column=4)
    
window = Tk()
window.title("Report Card")

Label(window,text="Name").grid(row=0,column=0)
Label(window,text="Roll.No").grid(row=1,column=0)
Label(window,text="Reg.No").grid(row=0,column=3)

e1 = Entry(window)
e1.grid(row=0,column=1)
e2 = Entry(window)
e2.grid(row=1,column=1)
e3 = Entry(window)
e3.grid(row=0,column=4)

title_list =["Srl.No","Subject","Grade","Sub Credit","Credit otained"]
column = 0
for i in title_list:
    Label(window,text=i).grid(row=2,column=column)
    column += 1

no_list =[1,2,3,4]
row = 3
for i in no_list:
    Label(window,text=i).grid(row=row,column=0)
    row += 1

subject_list =["CS 201","CS 202","MA 201","EC 201"]
row = 3
for i in subject_list:
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

credit_list =[4,4,3,4]
row = 3
for i in credit_list:
    Label(window,text=i).grid(row=row,column=3)
    row += 1

Label(window,text="Total credit").grid(row=7,column=3)
Label(window,text="SGPA").grid(row=8,column=3)

Button(window,text="Submit",fg="black",bg="blue",command=Submit).grid(row=8,column=1)

window.mainloop()
