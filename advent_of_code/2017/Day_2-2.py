import fileinput

sum = 0
for line in fileinput.input():
	list = line.split("\t")
	for i in range(0,len(list)-1):
		n = int(list[i])
		for j in range(i+1, len(list)):
			m = int(list[j])
			if n % m == 0:
				sum += n//m
			elif m % n == 0:
				sum += m//n
print(sum)