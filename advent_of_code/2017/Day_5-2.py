import fileinput

jumplist = []
for line in fileinput.input():
	jumplist.append(int(line))

i = 0
count = 0
while(i >= 0 and i < len(jumplist)):
	oldjump = jumplist[i]
	if oldjump >= 3:
		jumplist[i] -= 1
	else:
		jumplist[i] += 1
	i += oldjump
	count += 1
print(count)