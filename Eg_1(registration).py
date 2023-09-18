from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def valid():
    e1_value = str(e1.get())
    e2_value = str(e2.get())
    radio_value = str(radio.get())
    combo_value = str(comboVar.get())
    check1_value = str(Cvar1.get())
    check2_value = str(Cvar2.get())
    if(e1_value == "" or e2_value == "" or radio_value == " " or combo_value == "Select your country" or (check1_value == "0" and check2_value == "0")):
        messagebox.showinfo("Invalid Message Alert","Fields cannot be empty!")
    else:
        messagebox.showinfo("Success Message","successfully registered")

window = Tk()
window.geometry('500x500')
window.title("Registration Form")

radio = StringVar(window," ")

Label(window,text="Registration form",font=("bold","18")).grid(row=0,column=0,columnspan=3)
Label(window,text="Full Name").grid(row=1,column=0)
Label(window,text="Email").grid(row=2,column=0)
Label(window,text="Gender").grid(row=3,column=0)
Label(window,text="Country").grid(row=4,column=0)
Label(window,text="Programming").grid(row=5,column=0)

e1 = Entry(window)
e1.grid(row=1,column=1,columnspan=2)
e2 = Entry(window)
e2.grid(row=2,column=1,columnspan=2)
r1 = Radiobutton(window,text="Male",variable=radio,value="Male")
r1.grid(row=3,column=1)
r2 = Radiobutton(window,text="Female",variable=radio,value="Female")
r2.grid(row=3,column=2)
comboVar = StringVar()
combo = ttk.Combobox(window,values=["Myanmar", "English"],textvariable=comboVar)
combo.set("Select your country")
combo.grid(row=4,column=1,columnspan=2)
Cvar1 = IntVar()
cb1 = Checkbutton(window,text="C++",variable=Cvar1,onvalue=1,offvalue=0)
cb1.grid(row=5,column=1)
Cvar2 = IntVar()
cb2 = Checkbutton(window,text="Python",variable=Cvar2,onvalue=1,offvalue=0)
cb2.grid(row=5,column=2)
b = Button(window,text="Submit",bg="green",fg="white",width=20,command=valid)
b.grid(row=6,column=0,columnspan=3)

window.mainloop()
