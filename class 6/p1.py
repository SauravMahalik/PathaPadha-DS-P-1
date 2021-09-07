d={"a":1, "b":2,"c":3}
val = eval(input("Enter the value to be searched"))
for i in d:
    if d[i]==val:
        print("Value found")
        break;
else:
    print("Value does not exist")