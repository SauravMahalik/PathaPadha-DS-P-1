y={'saurav':40,'muskan':2,'mandip':1,'suman':3, 'rajdeep':42} 
                                         
l=list(y.items())   
l.sort()           
print('Ascending order is',l) 

l=list(y.items())
l.sort(reverse=True) 
print('Descending order is',l)

dict=dict(l) 

print("Dictionary",dict)