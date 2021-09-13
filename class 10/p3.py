class Employee:
    def __init__(abc,name):
        abc.name=name

    def change_name(abc,name2):
        abc.name=name2
        return abc.name

n=input("Enter the name ")
e=Employee(n)

print("The original name is ",e.name)
print("The new name is",e.change_name("john"))