from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def submit():
    if str(e1.get()) == " " or str(e2.get()) == " " or str(r_var.get()) == " " or str(combo.get()) == " " or (str(c1_var.get()) == " " and str(c2_var.get()) == " "):
        messagebox.showerror("Invalid Message Alert","Fields cannot be empty")
    else:
        messagebox.showinfo("Success Message","Information are registered")

window = Tk()
window.title("Registration Form")
window.geometry('250x200')

Label(window,text="Regristraton form",font=("Arial", 18)).grid(row=0,column=0,columnspan=3)
Label(window,text="Full Name").grid(row=1,column=0,sticky=W)
Label(window,text="Email").grid(row=2,column=0,sticky=W)
Label(window,text="Gender").grid(row=3,column=0,sticky=W)
Label(window,text="Country").grid(row=4,column=0,sticky=W)
Label(window,text="Programming").grid(row=5,column=0,sticky=W)

e1 = Entry(window)
e1.grid(row=1,column=1,columnspan=2,sticky=W)
e2 = Entry(window)
e2.grid(row=2,column=1,columnspan=2,sticky=W)

r_var = StringVar(window," ")
Radiobutton(window,text="Male",variable=r_var,value="Male").grid(row=3,column=1,sticky=W)
Radiobutton(window,text="Female",variable=r_var,value="Female").grid(row=3,column=2,sticky=W)

combo = ttk.Combobox(window,values=["Myanmar","English"])
combo.set("Myanmar")
combo.grid(row=4,column=1,columnspan=2,sticky=W)

c1_var = StringVar(window," ")
c1 = Checkbutton(window,text="C++",variable=c1_var,onvalue="C++",offvalue=" ")
c1.grid(row=5,column=1,sticky=W)
c2_var = StringVar(window," ")
c2 = Checkbutton(window,text="Python",variable=c2_var,onvalue="Python",offvalue=" ")
c2.grid(row=5,column=2,sticky=W)

Button(window,text="Submit",fg="white", bg="green",width=20,command=submit).grid(row=6,column=0,columnspan=3)
                                    

window.mainloop()
