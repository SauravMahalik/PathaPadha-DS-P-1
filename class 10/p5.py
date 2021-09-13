import tkinter
from tkinter import messagebox

def show():
    name=e1.get()
    passw=e2.get()
    result=name+" "+passw
    messagebox.showinfo("Details",result)

root=tkinter.Tk()

l=tkinter.Label(root,text="Enter Name")
l2=tkinter.Label(root,text="Enter Password")
e1=tkinter.Entry(root)
e2=tkinter.Entry(root)
b=tkinter.Button(root,text="Click",command=show)

l.grid(row=0,column=0)
l2.grid(row=1,column=0)

e1.grid(row=0,column=0)
e2.grid(row=1,column=1)

b.grid(row=2,column=1)

root.mainloop()