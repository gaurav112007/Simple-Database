from Tkinter import *
from math import *


def show_entry_fields():
    
   print("Name: %s\nAge: %d\nSalary: %d" % (e1.get(), int(e2.get()), int(e3.get())))

master = Tk()
Label(master, text="Name").grid(row=0)
Label(master, text="Age").grid(row=1)
Label(master, text="Salary").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

def evaluate(event):
    res.configure(text = "Total: " + str(eval(entry.get())))
w = Tk()
Label(w, text="Your Expression:").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()

mainloop( )
