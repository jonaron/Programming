import fileinput

memory = [int(x) for x in fileinput.input()[0].split("\t")]
dict = {}
count, l = 0, len(memory)
while str(memory) not in dict:
	dict[str(memory)] = count
	max, maxi = 0, -1
	for i in range(0, l):
		if memory[i] > max:
			max, maxi = memory[i], i
	memory[maxi] = 0
	for i in range(maxi+1, maxi+max+1):
		memory[i%l] += 1
	count += 1
print(count, count-dict[str(memory)])