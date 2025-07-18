from tkinter import *
import calendar

text=calendar.calendar(2025)

root=Tk()
root.geometry("550x650")
root.title("CALENDAR")

icon=PhotoImage(file="cal_icon.png")
root.iconphoto(False,icon)

label1=Label(root,text="CALENDAR",bg="dark gray",font="times 28 bold")
label1.grid(row=1,column=1)
root.config(bg="white")
l1=Label(root,text=text,font="consolas 10 bold")
l1.grid(row=2,column=1,padx=20)
root.mainloop()