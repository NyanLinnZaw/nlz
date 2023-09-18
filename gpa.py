from tkinter import * 

window = Tk()
window.title("GPA Calculator")

final_gpa = StringVar()
s1_credit = StringVar()
s2_credit = StringVar()
s3_credit = StringVar()
s4_credit = StringVar()
s5_credit = StringVar()
s6_credit = StringVar()
total_credit = StringVar()

def GPA():
    gpa = {"A+":4,"A":4,"A-":3.7,
       "B+":3.3,"B":3,"B-":2.7,
       "C+":2.3,"C":2,"C-":1.7,
       "D+":1.3,"D":1,"D-":0.7,
       "F":0}
    s1 = str(e4.get())
    s2 = str(e5.get())
    s3 = str(e6.get())
    s4 = str(e7.get())
    s5 = str(e8.get())
    s6 = str(e9.get())
    for key in gpa.keys():
        if s1 == key:
            r1 = int(gpa[key])
    for key in gpa.keys():
        if s2 == key:
            r2 = int(gpa[key])
    for key in gpa.keys():
        if s3 == key:
            r3 = int(gpa[key])
    for key in gpa.keys():
        if s4 == key:
            r4 = int(gpa[key])
    for key in gpa.keys():
        if s5 == key:
            r5 = int(gpa[key])
    for key in gpa.keys():
        if s6 == key:
            r6 = int(gpa[key])
    gpa = ((r1*2) + (r2*4) + (r3*4) + (r4*4) + (r5*4) + (r6*4)) / 22
    t_credit = ((r1*2) + (r2*4) + (r3*4) + (r4*4) + (r5*4) + (r6*4))
    s1_crd = float(r1*2)
    s2_crd = float(r2*4)
    s3_crd = float(r3*4)
    s4_crd = float(r4*4)
    s5_crd = float(r5*4)
    s6_crd = float(r6*4)
    final_gpa.set(gpa)
    total_credit.set(t_credit)
    s1_credit.set(s1_crd)
    s2_credit.set(s2_crd)
    s3_credit.set(s3_crd)
    s4_credit.set(s4_crd)
    s5_credit.set(s5_crd)
    s6_credit.set(s6_crd)

Label(window,text="Name").grid(row=0,column=0)
e1 = Entry(window)
e1.grid(row=0,column=1)
Label(window,text="Roll.No").grid(row=1,column=0)
e2 = Entry(window)
e2.grid(row=1,column=1)
Label(window,text="Reg.No").grid(row=0,column=3)
e3 = Entry(window)
e3.grid(row=0,column=4)

Label(window,text="Srl.No").grid(row=2,column=0)
Label(window,text="Subject").grid(row=2,column=1)
Label(window,text="Grade").grid(row=2,column=2)
Label(window,text="Sub Credit").grid(row=2,column=3)
Label(window,text="Credit obtained").grid(row=2,column=4)

Label(window,text="1").grid(row=3,column=0)
Label(window,text="English").grid(row=3,column=1)
e4 = Entry(window)
e4.grid(row=3,column=2)
Label(window,text="2").grid(row=3,column=3)

Label(window,text="2").grid(row=4,column=0)
Label(window,text="CST-3012").grid(row=4,column=1)
e5 = Entry(window)
e5.grid(row=4,column=2)
Label(window,text="4").grid(row=4,column=3)

Label(window,text="3").grid(row=5,column=0)
Label(window,text="CS-3022").grid(row=5,column=1)
e6 = Entry(window)
e6.grid(row=5,column=2)
Label(window,text="4").grid(row=5,column=3)

Label(window,text="4").grid(row=6,column=0)
Label(window,text="CS-3032").grid(row=6,column=1)
e7 = Entry(window)
e7.grid(row=6,column=2)
Label(window,text="4").grid(row=6,column=3)

Label(window,text="5").grid(row=7,column=0)
Label(window,text="CS-3042").grid(row=7,column=1)
e8 = Entry(window)
e8.grid(row=7,column=2)
Label(window,text="4").grid(row=7,column=3)

Label(window,text="6").grid(row=8,column=0)
Label(window,text="CST-3112").grid(row=8,column=1)
e9 = Entry(window)
e9.grid(row=8,column=2)
Label(window,text="4").grid(row=8,column=3)

b = Button(window,text="Submit",bg="green",fg="black",command=GPA)
b.grid(row=10,column=1)

Label(window,text="Total Credit").grid(row=9,column=3)
Label(window,text="GPA").grid(row=10,column=3)

Label(window,textvariable=s1_credit).grid(row=3,column=4)
Label(window,textvariable=s2_credit).grid(row=4,column=4)
Label(window,textvariable=s3_credit).grid(row=5,column=4)
Label(window,textvariable=s4_credit).grid(row=6,column=4)
Label(window,textvariable=s5_credit).grid(row=7,column=4)
Label(window,textvariable=s6_credit).grid(row=8,column=4)
Label(window,textvariable=total_credit).grid(row=9,column=4)
Label(window,textvariable=final_gpa).grid(row=10,column=4)

window.mainloop()