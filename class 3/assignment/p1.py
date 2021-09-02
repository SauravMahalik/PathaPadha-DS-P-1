String = "Saurav Mahalik"
  
count = 0
for i in String:
      count = count + 1
newString = String[ 0:2 ] + String [count - 2: count ] 

print("Initial string = " + String)
print("New String = "+ newString)