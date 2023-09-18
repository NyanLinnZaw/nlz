from tkinter import *
from tkinter import ttk

def Next():
   print(str(check1_var.get()))
   print(str(check2_var.get()))
   print(str(check3_var.get()))
   print(str(check4_var.get()))
   print(str(radio_var.get()))

window = Tk()
window.title("Food Order Form")
window.geometry("400x400")

Label(window,text="Food Order Form",font=("Helvetic", 20),bd=10).pack()
line = ttk.Separator(orient=HORIZONTAL)
line.pack(fill='x')
Label(window,text="What would you like to order?").pack(anchor='w')
check1_var = StringVar()
Checkbutton(window,text="Sandwich",variable=check1_var,onvalue="Sandwich",offvalue="").pack(anchor='w')
check2_var = StringVar()
Checkbutton(window,text="Slad",variable=check2_var,onvalue="Slad",offvalue="").pack(anchor='w')
check3_var = StringVar()
Checkbutton(window,text="Soup",variable=check3_var,onvalue="Soup",offvalue="").pack(anchor='w')
check4_var = StringVar()
Checkbutton(window,text="Pizza",variable=check4_var,onvalue="Pizza",offvalue="").pack(anchor='w')

Label(window,text="How do you want to pay?").pack(anchor='w')
radio_var =  StringVar(window," ")
Radiobutton(window,text="KBZpay",variable=radio_var,value="KBZpay").pack(anchor='w')
Radiobutton(window,text="Credid Card",variable=radio_var,value="Credid Card").pack(anchor='w')
Radiobutton(window,text="Other",variable=radio_var,value="Other").pack(anchor='w')

Button(window,text="Next",command=Next,width=10).pack()

window.mainloop()
