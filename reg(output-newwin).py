from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def successful():
    info1 = str(e1.get())
    info2 = str(e2.get())
    info3 = str(e3.get())
    info4 = str(e4.get())
    combo1 = str(combo.get())
    r_info = str(var.get())
    c1_info = str(cvar1.get())
    c2_info = str(cvar2.get())
    if(info1 == "" or info2 == "" or info3 == "" or info4 == "" or
       combo1 == "" or r_info == "" or c1_info == "" and c1_info == ""):
        messagebox.showinfo("Invalid Message Alert","Fields cannot be empty")
    else:
        messagebox.showinfo("Success Message","Successfully registered")

class next():
    def __init__(self):
        self.top = Tk()
        Label(self.top,text=str(e1.get())).grid(row=0,column=0)
        Label(self.top,text=str(e2.get())).grid(row=1,column=0)
        Label(self.top,text=str(e3.get())).grid(row=2,column=0)
        Label(self.top,text=str(e4.get())).grid(row=3,column=0)
        Label(self.top,text=str(var.get())).grid(row=4,column=0)
        Label(self.top,text=str(cvar1.get())).grid(row=5,column=0)
        Label(self.top,text=str(cvar2.get())).grid(row=5,column=1)
        Label(self.top,text=str(combo.get())).grid(row=6,column=0)
        self.top.mainloop()


window = Tk()
window.geometry("300x400")

e1var = StringVar()
e2var = StringVar()
e3var = StringVar()
e4var = StringVar()
combo_var = StringVar()
var = StringVar(window," ")
cvar1 = StringVar(window," ")
cvar2 = StringVar(window," ")

Label(window,text="Name").grid(row=0,column=0)
Label(window,text="NRC No").grid(row=1,column=0)
Label(window,text="Class").grid(row=2,column=0)
Label(window,text="Email").grid(row=3,column=0)
Label(window,text="Gender").grid(row=4,column=0)
Label(window,text="Country").grid(row=5,column=0)
Label(window,text="Language").grid(row=6,column=0)

e1 = Entry(window,width=30)
e1.grid(row=0,column=1,columnspan=2)
e2 = Entry(window,width=30)
e2.grid(row=1,column=1,columnspan=2)
e3 = Entry(window,width=30)
e3.grid(row=2,column=1,columnspan=2)
e4 = Entry(window,width=30)
e4.grid(row=3,column=1,columnspan=2)
r = Radiobutton(window,text="Male",variable=var,value="M")
r.grid(row=4,column=1,sticky=W)
r = Radiobutton(window,text="Female",variable=var,value="F")
r.grid(row=4,column=2,sticky=W)
combo = ttk.Combobox(window,values=["Myanmar","Singapore","Thailand","China"])
combo.grid(row=5,column=1,columnspan=2)
c = Checkbutton(window,text="English",variable=cvar1,onvalue="Eng",offvalue="No")
c.grid(row=6,column=1,sticky=W)
c = Checkbutton(window,text="Myanmar",variable=cvar2,onvalue="MM",offvalue="No")
c.grid(row=6,column=2,sticky=W)
Button(window,text="Submit",width=20,command=successful).grid(row=7,column=1,columnspan=2)
Button(window,text="Show info",width=20,command=next).grid(row=8,column=1,columnspan=2)

window.mainloop()