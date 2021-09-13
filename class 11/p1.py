from tkinter import *
from tkinter import messagebox

def selected():
    if chk1.get()==1 and chk2.get()==1 and chk3.get()==1:
        print("Python, Java, C++")
    elif chk1.get()==1:
        print("Python Selected")
    elif chk1.get()==1:
        print("Java Selected")
    else:
        print("C++ Selected")

root=Tk()

chk1=IntVar()
chk2=IntVar()
chk3=IntVar()

chk1=Checkbutton(root,text="Python",variable=chk1,offvalue=0,onvalue=1)
chk2=Checkbutton(root,text="Java",variable=chk2,offvalue=0,onvalue=1)
chk3=Checkbutton(root,text="C++",variable=chk3,offvalue=0,onvalue=1)
b=Button(root,text="Show",command=selected)

chk1.pack()
chk2.pack()
chk3.pack()

b.pack()
root.mainloop()