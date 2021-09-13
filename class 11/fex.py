from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox


class Student(Tk):#inheriting Tk() class
    def __init__(self):
        super().__init__() #calling parent class constructor

    def add_student(self):
        self.add=Toplevel(self)
        self.name_lbl=Label(self.add,text="Enter Name")
        self.name_entry=Entry(self.add)

        self.pass_lbl=Label(self.add,text="Enter Password")
        self.pass_entry=Entry(self.add)

        self.reg=Button(self.add,text="Register",command=self.register_student)

        self.name_lbl.grid(row=0,column=0)
        self.name_entry.grid(row=0,column=1)

        self.pass_lbl.grid(row=1,column=0)
        self.pass_entry.grid(row=1,column=1)

        self.reg.grid(row=2,column=0)
        self.add.mainloop()

    def register_student(self):
        n=self.name_entry.get()
        p=self.pass_entry.get()

        sql="select * from user_data where name=%s and password=%s"
        val=(n,p)
        cur.execute(sql,val)
        result=cur.fetchone()
        if(result):
            messagebox.showerror("Record Exists","Retry!!")
        else:
        

            sql2="insert into user_data(name,password)values(%s,%s)"
            val2=(n,p)
            cur.execute(sql2,val2)
            con.commit()
            result2=cur.rowcount
            if(result2):
                messagebox.showinfo("Success","Registered Successfully")
            else:
                messagebox.showerror("Error","Not Registered!!Try again")


    def login(self):
        self.log=Toplevel(self)
        self.name_lbl=Label(self.log,text="Enter Name")
        self.name_entry=Entry(self.log)

        self.pass_lbl=Label(self.log,text="Enter Password")
        self.pass_entry=Entry(self.log)

        self.reg=Button(self.log,text="Login",command=self.login_student)

        self.name_lbl.grid(row=0,column=0)
        self.name_entry.grid(row=0,column=1)

        self.pass_lbl.grid(row=1,column=0)
        self.pass_entry.grid(row=1,column=1)

        self.reg.grid(row=2,column=0)
        self.log.mainloop()


    def login_student(self):
        n=self.name_entry.get()
        p=self.pass_entry.get()
        sql="select * from user_data where name=%s and password=%s"
        val=(n,p)
        cur.execute(sql,val)
        result=cur.fetchall()
        if(result):
            messagebox.showinfo("Succes","Login Successfull")
            self.profile()
            


    def profile(self):
        self.welcome=Toplevel(self)
        self.w_lbl=Label(self.welcome,text="Welcome to the System",font=("Arial",18))
        self.w_lbl.pack()
        self.welcome.mainloop()
        

        
        




con=mysql.connect(host="localhost",user="root",password="",db="myproject")
cur=con.cursor()
s=Student()

main_screen=Label(s,text="Student Management System",font=('Arial',18))
add_btn=Button(s,text="Add New Student",font=('Arial',12),command=s.add_student)
Login_btn=Button(s,text="Login User",font=('Arial',12),command=s.login)
show_btn=Button(s,text="Show Students",font=('Arial',12))
main_screen.pack(side="top")
add_btn.pack()
show_btn.pack()
Login_btn.pack()
s.mainloop()
    
