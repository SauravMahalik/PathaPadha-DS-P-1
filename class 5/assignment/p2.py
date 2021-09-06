def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
print('unique elements are')
print(unique_list([1,2,4,5,4,5,6,9,10])) 