import math

input = 312051
circle = (math.sqrt(input-1)+1)//2
low = (circle*2-1)**2+circle
while input > low+circle:
	input -= 2*circle
if input > low:
	print(input-low+circle)
else:
	print(low-input+circle)