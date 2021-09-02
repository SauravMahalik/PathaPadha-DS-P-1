string = input("Enter a String: ")
countUC = 0
countLC = 0

for i in string:
      if(i.islower()):
            countLC += 1
      elif(i.isupper()):
            countUC += 1
print("The number of lowercase characters is:")
print(countLC)
print("The number of uppercase characters is:")
print(countUC)


