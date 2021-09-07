d = {0:30, 1:40, 2:10, 3:20, 4:59, 5:60}
for i in sorted(d,key=d.get):
    print(i,d[i])