def selection():
    
    if gender.get()==1:
        print("Male")
    elif gender.get()==2:
        print("Female")
     
root=Tk()
root.configure(background="red")

gender=IntVar()

R1=Radiobutton(root,text="Male",variable=gender,value=1,bg="green",fg="yellow",command=selection)
R2=Radiobutton(root,text="Female",variable=gender,value=2,command=selection)

cols=("1","2")
trv=ttk.Treeview(root,columns=cols,show='headings',height=2)

trv.heading("1",text="Name")
trv.heading("2",text="Age")
lst=[]

lst.append(['Arun',10])
lst.append(['Priya',12])

for i in lst:
    trv.insert('','end',values=i)
trv.bind("<<TreeviewSelect>>",item_selected)
def item_selected(event):
    for i in trv.selection():
        
        item=trv.item(i)
    print(item)
trv.bind("<Double-1>",item_selected)