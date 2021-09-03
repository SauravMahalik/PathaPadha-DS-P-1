list = [1,2,3,4,5]
n=int(input("Enter element: "))
for i in range(0,len(list)):
    if(n==list[i]):
        print("Element found at position",i+1)
        break;
else:
    print("Element not found")
