from tkinter import *

def printResult():
    c1_value = str(check1.get())
    c2_value = str(check2.get())
    c3_value = str(check3.get())
    c4_value = str(check4.get())
    if c1_value:
        print(c1_value)
    if c2_value:
        print(c2_value)
    if c3_value:
        print(c3_value)
    if c4_value:
        print(c4_value)

    radio_value = str(radio.get())
    print(radio_value)

    
    

window = Tk()

Label(window,text="Food Order Form", font=("bold",20)).grid(row=0,column=0,columnspan=3)
Label(window,text="What would you like to order?").grid(row=2,column=0,columnspan=2)
check1 = StringVar(window," ")
c1 = Checkbutton(window,text="Sandwich",variable=check1,onvalue="Sandwich",offvalue="")
c1.grid(row=3,column=0,sticky=W)
check2 = StringVar()
c2 = Checkbutton(window,text="Slad",variable=check2,onvalue="Slad",offvalue="")
c2.grid(row=4,column=0,sticky=W)
check3 = StringVar()
c3 = Checkbutton(window,text="Soup",variable=check3,onvalue="Soup",offvalue="")
c3.grid(row=5,column=0,sticky=W)
check4 = StringVar()
c4 = Checkbutton(window,text="Pizza",variable=check4,onvalue="Pizza",offvalue="")
c4.grid(row=6,column=0,sticky=W)

Label(window,text="How do you want to pay?").grid(row=7,column=0,columnspan=2)
radio = StringVar(window," ")
r1 = Radiobutton(window,text="KBZpay",variable=radio,value="KBZpay")
r1.grid(row=8,column=0,sticky=W)
r2 = Radiobutton(window,text="Credit Card",variable=radio,value="Credit Card")
r2.grid(row=9,column=0,sticky=W)
r3 = Radiobutton(window,text="Other",variable=radio,value="Other")
r3.grid(row=10,column=0,sticky=W)

Button(window,text="Next",command=printResult,width=10,bg="gray",fg="black").grid(row=11,column=0,columnspan=3)
result = StringVar()
Label(window,textvariable=result).grid(row=12,column=0,columnspan=2)

window.mainloop()
