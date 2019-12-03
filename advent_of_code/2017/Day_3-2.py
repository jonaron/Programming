input = 312051
dict = {(0,0): 1}

def getValue(i,j):
	if (i,j) in dict:
		return dict[(i,j)]
	else:
		return 0

def addValue(i,j):
	return (getValue(i-1,j-1)+getValue(i-1,j)+getValue(i-1,j+1)+getValue(i,j+1)+getValue(i+1,j+1)+getValue(i+1,j)+getValue(i+1,j-1)+getValue(i,j-1))

k = 1
x = 0
y = 0
found = False
while(True):
	for i in range(0,k*2-1):
		x += 1
		v = addValue(x,y)
		if v > input:
			found = True
			print(v)
		else:
			dict[(x,y)] = v
	if found:
		break
	for i in range(0,k*2-1):
		y += 1
		v = addValue(x,y)
		if v > input:
			found = True
			print(v)
		else:
			dict[(x,y)] = v
	if found:
		break
	for i in range(0,k*2):
		x -= 1
		v = addValue(x,y)
		if v > input:
			found = True
			print(v)
		else:
			dict[(x,y)] = v
	if found:
		break
	for i in range(0,k*2):
		y -= 1
		v = addValue(x,y)
		if v > input:
			found = True
			print(v)
		else:
			dict[(x,y)] = v
	if found:
		break
	k += 1