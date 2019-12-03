import fileinput

sum = 0
for line in fileinput.input():
	list = line.split("\t")
	low = int(list[0])
	high = low
	for number in list:
		if int(number) < low:
			low = int(number)
		if int(number) > high:
			high = int(number)
	sum += high-low
print(sum)