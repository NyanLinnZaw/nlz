from tkinter import *
from tkinter import messagebox

def clearAll():
    e_day.delete(0,END)
    e_month.delete(0,END)
    e_year.delete(0,END)
    e_Years.delete(0,END)
    e_Months.delete(0,END)
    e_Days.delete(0,END)
    e_givenday.delete(0,END)
    e_givenmonth.delete(0,END)
    e_givenyear.delete(0,END)

def checkError():
    if(e_day.get()=="" or e_month.get()=="" or e_year.get()=="" or
        e_givenday.get()=="" or e_givenmonth.get()=="" or e_givenyear.get()==""):
        messagebox.showerror("Input Error")
        clearAll()
        return -1
    
def calculateAge():
    value = checkError()
    if value == -1:
        return
    else:
        birth_day = int(e_day.get())
        birth_month = int(e_month.get())
        birth_year = int(e_year.get())
        now_day = int(e_givenday.get())
        now_month = int(e_givenmonth.get())
        now_year = int(e_givenyear.get())

        month = [31,28,31,30,31,30,31,31,30,31,30,31]

        if(birth_day > now_day):
            now_month = now_month - 1
            now_day = now_day + month[now_month - 1]

        if(birth_month > now_month):
            now_year = now_year - 1
            now_month = now_month + 12

        calculated_day = now_day - birth_day
        calcualted_month = now_month - birth_month
        calculated_year = now_year - birth_year

        e_Days.insert(0,str(calculated_day))
        e_Months.insert(0,str(calcualted_month))
        e_Years.insert(0,str(calculated_year))

window = Tk()
window.geometry("525x260")

window.configure(bg="light green")

DOB = Label(window,text="Date Of Birth",bg="blue")
DOB.grid(row=0,column=1)
day = Label(window,text="Day",bg="light green")
day.grid(row=1,column=0)
month = Label(window,text="Month",bg="light green")
month.grid(row=2,column=0)
year = Label(window,text="Year",bg="light green")
year.grid(row=3,column=0)
e_day = Entry(window)
e_day.grid(row=1,column=1)
e_month = Entry(window)
e_month.grid(row=2,column=1)
e_year = Entry(window)
e_year.grid(row=3,column=1)

Age = Button(window,text="Resultant Age",bg="red",command=calculateAge)
Age.grid(row=4,column=3)
Years = Label(window,text="Years",bg="light green")
Years.grid(row=5,column=3)
e_Years = Entry(window)
e_Years.grid(row=6,column=3)
Months = Label(window,text="Months",bg="light green")
Months.grid(row=7,column=3)
e_Months = Entry(window)
e_Months.grid(row=8,column=3)
Days = Label(window,text="Days",bg="light green")
Days.grid(row=9,column=3)
e_Days = Entry(window)
e_Days.grid(row=10,column=3)

givenDate = Label(window,text="Given Date",bg="blue")
givenDate.grid(row=0,column=5)
given_day = Label(window,text="Given Day",bg="light green")
given_day.grid(row=1,column=4)
given_month = Label(window,text="Given Month",bg="light green")
given_month.grid(row=2,column=4)
given_year = Label(window,text="Given Year",bg="light green")
given_year.grid(row=3,column=4)
e_givenday = Entry(window)
e_givenday.grid(row=1,column=5)
e_givenmonth = Entry(window)
e_givenmonth.grid(row=2,column=5)
e_givenyear = Entry(window)
e_givenyear.grid(row=3,column=5)

button = Button(window,text="Clear All",bg="red",fg="black",command=clearAll)
button.grid(row=11,column=3)


window.mainloop()
