import random

def Rand(start, end, num):
	res = []
	for j in range(num):
		res.append(random.randint(start, end))
	return res
num = 10
start = 15
end = 30
print(Rand(start, end, num))
