import fileinput

input = fileinput.input()[0]
sum = 0
for i in range(0, len(input)-1):
	if input[i] == input[i+1]:
		sum += int(input[i])
if input[-1] ==	input[0]:
	sum += int(input[-1])
print(sum)