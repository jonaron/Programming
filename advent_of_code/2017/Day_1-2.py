import fileinput

input = fileinput.input()[0]
sum = 0
halflen = len(input)//2
for i in range(0,halflen):
	if input[i] == input[i+halflen]:
		sum += int(input[i])*2
print(sum)