l = models = [{'make':'Nokia','model':216,'color':'Black'},{'make':'Mi Max','model':696,'color':'Silver'}]

res =filter(lambda x:x["model"]>10,l)
print(list(res))