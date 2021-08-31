max = 30
et = 0
ot = 0
 
for n in range(20, max + 1):
    if(n % 2 == 0):
        et = et + n
    else:
        ot = ot + n
 
print("The Sum of Even Numbers from 20 to {0} = {1}".format(n, et))
print("The Sum of Odd Numbers from 20 to {0} = {1}".format(n, ot))