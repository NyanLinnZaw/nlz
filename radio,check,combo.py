from tkinter import *
from tkinter import ttk

class SimpleGUI(Tk):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):

        def get_states():
            Label(self,text=str(self.c1_var.get())).grid(row=0,column=1)
            Label(self,text=str(self.c2_var.get())).grid(row=0,column=2)
            Label(self,text=str(self.radio_var.get())).grid(row=1,column=1)
            Label(self,text=str(self.combo_var.get())).grid(row=2,column=1)
            

        self.title("Personal Details")
        self.geometry("700x350")
        
        Label(self,text="Check box state").grid(row=0,column=0,sticky=W)
        Label(self,text="Radio Button state").grid(row=1,column=0,sticky=W)
        Label(self,text="Combo box state").grid(row=2,column=0,sticky=W)
        
        self.c1_var = StringVar()
        Checkbutton(self,text="Driver",variable=self.c1_var,onvalue="Driver",offvalue="").grid(row=3,column=0,sticky=W)
        self.c2_var = StringVar()
        Checkbutton(self,text="Passenger",variable=self.c2_var,onvalue="Passenger",offvalue="").grid(row=4,column=0,sticky=W)
        
        self.combo_var = StringVar()
        self.combo = ttk.Combobox(self,textvariable=self.combo_var,values=["Swimming","Walking","Hiking","Golfing","Fishing"])
        self.combo.set("Choose one")
        self.combo.grid(row=5,column=0)

        self.radio_var = StringVar(self," ")
        Radiobutton(self,text="Married",variable=self.radio_var,value="Married").grid(row=3,column=1,sticky=W)
        Radiobutton(self,text="Single",variable=self.radio_var,value="Single").grid(row=4,column=1,sticky=W)
        Radiobutton(self,text="Divorced",variable=self.radio_var,value="Divorced").grid(row=5,column=1,sticky=W)

        Button(self,text="Get states",command=get_states).grid(row=6,column=0,columnspan=2)


if __name__ == "__main__":
    window = SimpleGUI()
    window.mainloop()
